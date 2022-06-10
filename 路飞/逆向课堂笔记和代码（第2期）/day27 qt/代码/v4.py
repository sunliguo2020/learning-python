import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtWidgets import QMessageBox, QMenu
from utils.dialog import LogDialog

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

STATUS_MAPPING = {
    0: "初始化中",
    1: "待执行",
    2: "正在执行",
    3: "完成并提醒",
    10: "异常并停止",
    11: "初始化失败",
}

RUNNING = 1
STOPPING = 2
STOP = 3


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.switch = STOP

        # 控件
        self.txt_asin = None

        # 窗体标题和尺寸
        self.setWindowTitle('NB的xx系统')

        # 窗体的尺寸
        self.resize(1228, 450)

        # 窗体位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 创建布局
        layout = QVBoxLayout()
        layout.addLayout(self.init_header())
        layout.addLayout(self.init_form())
        layout.addLayout(self.init_table())
        layout.addLayout(self.init_footer())

        # 给窗体设置元素的排列方式
        self.setLayout(layout)

    def init_header(self):
        # 1.创建顶部菜单布局
        header_layout = QHBoxLayout()

        # 1.1 创建按钮，加入 header_layout
        btn_start = QPushButton("开始")
        btn_start.clicked.connect(self.event_start_click)
        header_layout.addWidget(btn_start)

        btn_stop = QPushButton("停止")
        btn_stop.clicked.connect(self.event_stop_click)
        header_layout.addWidget(btn_stop)

        # 弹簧
        header_layout.addStretch()

        return header_layout

    def init_form(self):
        # 2.创建上面标题布局
        form_layout = QHBoxLayout()

        # 2.1 输入框
        txt_asin = QLineEdit()
        txt_asin.setText("B07YN82X3B=100")
        txt_asin.setPlaceholderText("请输入商品ID和价格，例如：B0818JJQQ8=88")
        self.txt_asin = txt_asin
        form_layout.addWidget(txt_asin)

        # 2.2 添加按钮
        btn_add = QPushButton("添加")
        btn_add.clicked.connect(self.event_add_click)
        form_layout.addWidget(btn_add)

        return form_layout

    def init_table(self):
        # 3.创建中间的表格
        table_layout = QHBoxLayout()

        # 3.1 创建表格
        self.table_widget = table_widget = QTableWidget(0, 8)
        table_header = [
            {"field": "asin", "text": "ASIN", 'width': 120},
            {"field": "title", "text": "标题", 'width': 150},
            {"field": "url", "text": "URL", 'width': 400},
            {"field": "price", "text": "底价", 'width': 100},
            {"field": "success", "text": "成功次数", 'width': 100},
            {"field": "error", "text": "503次数", 'width': 100},
            {"field": "status", "text": "状态", 'width': 100},
            {"field": "frequency", "text": "频率（N秒/次）", 'width': 100},
        ]
        for idx, info in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(idx, item)
            table_widget.setColumnWidth(idx, info['width'])

        # 3.2 初始化表格数据
        # 读取数据文件
        import json
        file_path = os.path.join(BASE_DIR, "db", "db.json")
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = f.read()
        data_list = json.loads(data)

        current_row_count = table_widget.rowCount()  # 当前表格有多少行
        for row_list in data_list:
            table_widget.insertRow(current_row_count)

            # row_list # ['B08166SLDF', 'AMD er', 'https://www.amazon.', 300.0, 0, 166, 1, 5]
            # 写真是数据
            for i, ele in enumerate(row_list):
                ele = STATUS_MAPPING[ele] if i == 6 else ele
                cell = QTableWidgetItem(str(ele))
                if i in [0, 4, 5, 6]:
                    # 不可修改
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                table_widget.setItem(current_row_count, i, cell)

            current_row_count += 1

        # # 开启右键复制功能，在表格中点击右键时，自动触发 right_menu 函数
        table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        table_widget.customContextMenuRequested.connect(self.table_right_menu)

        table_layout.addWidget(table_widget)
        return table_layout

    def table_right_menu(self, pos):

        # 只有选中一行时，才支持右键
        selected_item_list = self.table_widget.selectedItems()
        if len(selected_item_list) == 0:
            return

        menu = QMenu()
        item_copy = menu.addAction("复制")
        item_log = menu.addAction("查看日志")
        item_log_clear = menu.addAction("清除日志")

        # 选中了那个？
        action = menu.exec_(self.table_widget.mapToGlobal(pos))

        if action == item_copy:
            # 赋值当前型号 B08166SLDF
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_item_list[0].text())

        if action == item_log:
            # 查看日志，在对话框中显示日志信息
            # 获取选中的型号
            row_index = selected_item_list[0].row()
            asin = self.table_widget.item(row_index, 0).text().strip()

            dialog = LogDialog(asin)
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

        if action == item_log_clear:
            # 清空日志
            row_index = selected_item_list[0].row()
            asin = self.table_widget.item(row_index, 0).text().strip()
            file_path = os.path.join("log", "{}.log".format(asin))
            if os.path.exists(file_path):
                os.remove(file_path)

    def init_footer(self):
        # 2.底部菜单
        footer_layout = QHBoxLayout()

        self.label_status = label_status = QLabel("未检测", self)
        footer_layout.addWidget(label_status)

        footer_layout.addStretch()

        btn_reset = QPushButton("重新初始化")
        btn_reset.clicked.connect(self.event_reset_click)
        footer_layout.addWidget(btn_reset)

        btn_recheck = QPushButton("重新检测")
        footer_layout.addWidget(btn_recheck)

        btn_reset_count = QPushButton("次数清零")
        btn_reset_count.clicked.connect(self.event_reset_count_click)
        footer_layout.addWidget(btn_reset_count)

        btn_delete = QPushButton("删除检测项")
        btn_delete.clicked.connect(self.event_delete_click)
        footer_layout.addWidget(btn_delete)

        btn_alert = QPushButton("SMTP报警配置")
        btn_alert.clicked.connect(self.event_alert_click)
        footer_layout.addWidget(btn_alert)

        btn_proxy = QPushButton("代理IP")
        btn_proxy.clicked.connect(self.event_proxy_click)
        footer_layout.addWidget(btn_proxy)
        return footer_layout

    # 点击添加按钮
    def event_add_click(self):
        # 1.获取输入框中的内容
        text = self.txt_asin.text()
        text = text.strip()
        if not text:
            QMessageBox.warning(self, "错误", "商品的ASIN输入错误")
            return
        # B07YN82X3B=100
        asin, price = text.split("=")
        price = float(price)

        # 2.加入到表格中（型号、底价）
        new_row_list = [asin, "", "", price, 0, 0, 0, 5]

        current_row_count = self.table_widget.rowCount()  # 当前表格有多少行
        self.table_widget.insertRow(current_row_count)
        for i, ele in enumerate(new_row_list):
            ele = STATUS_MAPPING[ele] if i == 6 else ele
            cell = QTableWidgetItem(str(ele))
            if i in [0, 4, 5, 6]:
                # 不可修改
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_widget.setItem(current_row_count, i, cell)

        # 3.发送请求自动获取标题（爬虫获取数据）
        # 注意：不能再主线程中做爬虫的事，创建一个线程去做爬虫，爬取到数据再更新到窗体应用（信号）。
        from utils.threads import NewTaskThread

        thread = NewTaskThread(current_row_count, asin, self)
        thread.success.connect(self.init_task_success_callback)
        thread.error.connect(self.init_task_error_callback)
        thread.start()

        pass

    def init_task_success_callback(self, row_index, asin, title, url):
        # print( row_index, asin, title, url)
        # 更新标题
        cell_title = QTableWidgetItem(title)
        self.table_widget.setItem(row_index, 1, cell_title)

        # 更新URL
        cell_url = QTableWidgetItem(url)
        self.table_widget.setItem(row_index, 2, cell_url)

        # 更新状态
        cell_status = QTableWidgetItem(STATUS_MAPPING[1])
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 6, cell_status)

        # 输入框清空
        self.txt_asin.clear()

    def init_task_error_callback(self, row_index, asin, title, url):
        # print("错误",row_index, asin, title, url)
        # 更新标题
        cell_title = QTableWidgetItem(title)
        self.table_widget.setItem(row_index, 1, cell_title)

        # 更新URL
        cell_url = QTableWidgetItem(url)
        self.table_widget.setItem(row_index, 2, cell_url)

        # 更新状态
        cell_status = QTableWidgetItem(STATUS_MAPPING[11])
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 6, cell_status)

    # 点击重新初始化
    def event_reset_click(self):
        # 1.获取已经选中的行
        row_list = self.table_widget.selectionModel().selectedRows()
        if not row_list:
            QMessageBox.warning(self, "错误", "请选择要重新初始化的行")
            return
        # 2.获取每一行进行重新初始化
        for row_object in row_list:
            index = row_object.row()
            print("选中的行：", index)
            # 获取信号
            asin = self.table_widget.item(index, 0).text().strip()

            # 状态重新初始化
            cell_status = QTableWidgetItem(STATUS_MAPPING[0])
            cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_widget.setItem(index, 6, cell_status)

            # 创建线程去进行初始化动作
            from utils.threads import NewTaskThread

            thread = NewTaskThread(index, asin, self)
            thread.success.connect(self.init_task_success_callback)
            thread.error.connect(self.init_task_error_callback)
            thread.start()

    # 点击数量清零
    def event_reset_count_click(self):
        # 1.获取已经选中的行
        row_list = self.table_widget.selectionModel().selectedRows()
        if not row_list:
            QMessageBox.warning(self, "错误", "请选择要操作的行")
            return
        # 2.获取每一行进行重新初始化
        for row_object in row_list:
            index = row_object.row()
            # print("选中的行：", index)
            # # 获取信号
            # asin = self.table_widget.item(index, 0).text().strip()

            # 状态重新初始化
            cell_status = QTableWidgetItem(str(0))
            cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_widget.setItem(index, 4, cell_status)

            cell_status = QTableWidgetItem(str(0))
            cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_widget.setItem(index, 5, cell_status)

    # 点击删除
    def event_delete_click(self):
        # 1.获取已经选中的行
        row_list = self.table_widget.selectionModel().selectedRows()
        if not row_list:
            QMessageBox.warning(self, "错误", "请选择要操作的行")
            return

        # 2.翻转
        row_list.reverse()

        # 3.删除
        for row_object in row_list:
            index = row_object.row()
            self.table_widget.removeRow(index)

    # 点击邮件配置
    def event_alert_click(self):
        # 创建弹窗并在弹窗中进行设置

        from utils.dialog import AlertDialog

        dialog = AlertDialog()
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    # 点击代理
    def event_proxy_click(self):
        from utils.dialog import ProxyDialog

        dialog = ProxyDialog()
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    # 点击开始
    def event_start_click(self):
        if self.switch != STOP:
            QMessageBox.warning(self, "错误", "正在执行获取终止中，请勿重复操作")
            return
        self.switch = RUNNING

        # 1.为每一行创建一个线程去执行 （ 所有的线程记录）  [x,x,x,x,]
        from utils.scheduler import SCHEDULER

        SCHEDULER.start(
            BASE_DIR,
            self,
            self.task_start_callback,
            self.task_stop_callback,
            self.task_counter_callback,
            self.task_error_counter_callback
        )

        # 2.执行中
        self.update_status_message("执行中")

    def task_start_callback(self, row_index):
        # 对表格中的数据进行状态更新
        cell_status = QTableWidgetItem(STATUS_MAPPING[2])
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 6, cell_status)

    def task_stop_callback(self, row_index):
        cell_status = QTableWidgetItem(STATUS_MAPPING[1])
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 6, cell_status)

    def task_counter_callback(self, row_index):
        # 原有个数+1
        old_count = self.table_widget.item(row_index, 4).text().strip()
        new_count = int(old_count) + 1

        # 表格赋值
        cell_status = QTableWidgetItem(str(new_count))
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 4, cell_status)

    def task_error_counter_callback(self, row_index):
        # 原有个数+1
        old_count = self.table_widget.item(row_index, 5).text().strip()
        new_count = int(old_count) + 1

        # 表格赋值
        cell_status = QTableWidgetItem(str(new_count))
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 5, cell_status)

    # 点击停止
    def event_stop_click(self):
        if self.switch != RUNNING:
            QMessageBox.warning(self, "错误", "已停止或正在终止,请勿重复操作")
            return

        self.switch = STOPPING

        # 1.执行中的线程逐一终止
        from utils.scheduler import SCHEDULER

        SCHEDULER.stop()
        # 2.更新状态

    def update_status_message(self, message):
        if message == "已终止":
            self.switch = STOP
        self.label_status.setText(message)
        self.label_status.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
