# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nochange.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
'''
  禁止窗体显示最大化按钮及调整窗体大小
'''
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # 禁止显示最大化按钮及调整窗体大小
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "禁止窗体显示最大化按钮及调整窗体大小"))


# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程
