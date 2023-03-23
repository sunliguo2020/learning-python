# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'txtToAudio.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
'''
  将输入的字符串转换为语音文件
'''
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# 导入baidu-aip
try:
    from aip import AipSpeech
except ModuleNotFoundError:
    print('正在安装baidu-aip，请稍等...')
    os.system('pip install baidu-aip')  # 安装baidu-aip模块

APP_ID = '自己的百度云应用APPID'  # 设置自己创建百度云应用时的ID
API_KEY = '自己的百度云应用APIKey'  # 设置自己创建百度云应用时的APIKey
SECRET_KEY = '自己的百度云应用SECRETKey'  # 设置自己创建百度云应用时的SECRETKey

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 198)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 371, 151))
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 351, 121))
        self.textEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 170, 51, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 170, 51, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(130, 170, 61, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(200, 170, 61, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 160, 75, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文字转换为语音"))
        self.groupBox.setTitle(_translate("MainWindow", "文字转语音"))
        self.radioButton.setText(_translate("MainWindow", "女声"))
        self.radioButton_2.setText(_translate("MainWindow", "男声"))
        self.radioButton_3.setText(_translate("MainWindow", "度逍遥"))
        self.radioButton_4.setText(_translate("MainWindow", "度丫丫"))
        self.pushButton.setText(_translate("MainWindow", "语音合成"))
        # 关联“语音合成”按钮的方法
        self.pushButton.clicked.connect(self.txtToAudio)

    def txtToAudio(self):
        voice = 0
        if self.radioButton.isChecked():
            voice = 0  # 女声
        elif self.radioButton_2.isChecked():
            voice = 1  # 男声
        elif self.radioButton_3.isChecked():
            voice = 3  # 度逍遥
        elif self.radioButton_4.isChecked():
            voice = 4  # 度丫丫
        # 语音合成
        result = client.synthesis(self.textEdit.toPlainText(), 'zh', 3, {
            'vol': 5,
            'per': voice,
        })
        import time
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).replace('-', '').replace(':', '').replace(' ',
                                                                                                             '')  # 获取当前日期时间
        # 识别正确返回语音二进制，错误则返回dict
        if not isinstance(result, dict):
            with open(str(now) + '.mp3', 'wb') as f:
                f.write(result)
            QMessageBox.information(None, '提示', '文字已经转换为相应的MP3文件，请在当前项目路径中查看！', QMessageBox.Ok)
        else:
            QMessageBox.information(None, '警告', '转换失败，请确认转换的文本长度不超过1024字节（342个汉字）！', QMessageBox.Ok)


# 主方法
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
