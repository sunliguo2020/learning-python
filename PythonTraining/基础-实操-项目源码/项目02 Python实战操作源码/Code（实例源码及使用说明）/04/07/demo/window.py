# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 60, 100, 30))
        self.pushButton.setStyleSheet("background-image: url(:/png/img/import.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


import img_qc_rc
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 首先必须实例化QApplication类，作为GUI主程序入口
    MainWindow = QtWidgets.QMainWindow()  # 实例化QtWidgets.QMainWindow类，创建自带menu的窗体类型QMainWindow
    ui = Ui_MainWindow()  # 实例UI类
    ui.setupUi(MainWindow)  # 设置窗体UI
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())
