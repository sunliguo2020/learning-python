import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

STATUS_MAPPING = {
    0: "初始化中",
    1: "待执行",
    2: "正在执行",
    3: "完成并提醒",
    10: "异常并停止",
    11: "初始化失败",
}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

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
        header_layout.addWidget(btn_start)

        btn_stop = QPushButton("停止")
        header_layout.addWidget(btn_stop)

        # 弹簧
        header_layout.addStretch()

        return header_layout

    def init_form(self):
        # 2.创建上面标题布局
        form_layout = QHBoxLayout()

        # 2.1 输入框
        txt_asin = QLineEdit()
        txt_asin.setPlaceholderText("请输入商品ID和价格，例如：B0818JJQQ8=88")
        form_layout.addWidget(txt_asin)

        # 2.2 添加按钮
        btn_add = QPushButton("添加")
        form_layout.addWidget(btn_add)

        return form_layout

    def init_table(self):
        # 3.创建中间的表格
        table_layout = QHBoxLayout()

        # 3.1 创建表格
        table_widget = QTableWidget(0, 8)
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

        table_layout.addWidget(table_widget)
        return table_layout

    def init_footer(self):
        # 2.底部菜单
        footer_layout = QHBoxLayout()

        label_status = QLabel("未检测", self)
        footer_layout.addWidget(label_status)

        footer_layout.addStretch()

        btn_reinit = QPushButton("重新初始化")
        footer_layout.addWidget(btn_reinit)

        btn_recheck = QPushButton("重新检测")
        footer_layout.addWidget(btn_recheck)

        btn_reset_count = QPushButton("次数清零")
        footer_layout.addWidget(btn_reset_count)

        btn_delete = QPushButton("删除检测项")
        footer_layout.addWidget(btn_delete)

        btn_alert = QPushButton("SMTP报警配置")
        footer_layout.addWidget(btn_alert)

        btn_proxy = QPushButton("代理IP")
        footer_layout.addWidget(btn_proxy)
        return footer_layout


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
