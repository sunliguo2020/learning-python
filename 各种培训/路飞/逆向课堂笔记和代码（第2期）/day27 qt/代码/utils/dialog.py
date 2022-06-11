import os
import json

from PyQt5.QtWidgets import QVBoxLayout, QDialog, QPushButton, QLabel, QLineEdit, QMessageBox, QTextEdit, QHBoxLayout

from PyQt5.QtCore import Qt


class AlertDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_dict = {}
        self.init_ui()

    def init_ui(self):
        """
        初始化对话框
        :return:
        """
        self.setWindowTitle("报警邮件配置")
        self.resize(300, 270)

        layout = QVBoxLayout()

        form_data_list = [
            {"title": "SMTP服务器:", "filed": "smtp"},
            {"title": "发件箱:", "filed": "from"},
            {"title": "密码:", "filed": "pwd"},
            {"title": "收件人（多个用逗号分隔）:", "filed": "to"},
        ]

        # 读取文件中的配置
        old_alert_dict = {}
        alert_file_path = os.path.join("db", 'alert.json')
        if os.path.exists(alert_file_path):
            file_object = open(os.path.join("db", 'alert.json'), mode='r', encoding='utf-8')
            old_alert_dict = json.load(file_object)
            file_object.close()

        for item in form_data_list:
            lbl = QLabel()
            lbl.setText(item['title'])
            layout.addWidget(lbl)

            txt = QLineEdit()
            layout.addWidget(txt)
            filed = item['filed']
            if old_alert_dict and filed in old_alert_dict:
                txt.setText(old_alert_dict[filed])
            self.field_dict[item['filed']] = txt

        btn_save = QPushButton("保存")
        btn_save.clicked.connect(self.event_save_click)
        layout.addWidget(btn_save, 0, Qt.AlignRight)

        layout.addStretch(1)
        self.setLayout(layout)

    def event_save_click(self):
        data_dict = {}
        for key, filed in self.field_dict.items():
            value = filed.text().strip()
            if not value:
                QMessageBox.warning(self, "错误", "邮件报警项不能为空")
                return
            data_dict[key] = value

        # {'smtp': '123123', 'from': '123123', 'pwd': '123123', 'to': '123123123'}
        # print(data_dict)

        file_object = open(os.path.join("db", 'alert.json'), mode='w', encoding='utf-8')
        json.dump(data_dict, file_object)
        file_object.close()

        # 关闭对话框
        self.close()


class ProxyDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("配置代理IP")
        self.resize(500, 400)
        layout = QVBoxLayout()

        # 输入框
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("可用换行来设置多个代理IP，每个代理IP设置格式为：31.40.225.250:3128")

        # 读取本地文件
        file_path = os.path.join("db", "proxy.txt")
        all_proxy = ""
        if os.path.exists(file_path):
            with open(os.path.join("db", "proxy.txt"), mode='r', encoding='utf-8') as f:
                all_proxy = f.read()
        text_edit.setText(all_proxy)

        self.text_edit = text_edit
        layout.addWidget(text_edit)

        footer_config = QHBoxLayout()

        btn_save = QPushButton("重置")
        btn_save.clicked.connect(self.event_save_click)
        footer_config.addWidget(btn_save, 0, Qt.AlignRight)

        layout.addLayout(footer_config)

        self.setLayout(layout)

    def event_save_click(self):
        # PROXY.write()
        text = self.text_edit.toPlainText()

        # 写入到代理文件中
        with open(os.path.join("db", "proxy.txt"), mode='w', encoding='utf-8') as f:
            f.write(text)
        self.close()


class LogDialog(QDialog):
    def __init__(self, asin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.asin = asin

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("日志记录")
        self.resize(500, 400)
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setText("")

        layout.addWidget(text_edit)
        self.setLayout(layout)

        # 读取日志展示出来
        file_path = os.path.join("log", "{}.log".format(self.asin))
        if not os.path.exists(file_path):
            return

        with open(file_path,mode='r',encoding='utf-8') as f:
            content = f.read()
        text_edit.setText(content)
