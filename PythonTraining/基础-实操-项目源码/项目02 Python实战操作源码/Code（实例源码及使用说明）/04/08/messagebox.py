# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messagebox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
'''
  弹出不同种类的消息提示框
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 88)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "弹出不同种类的消息提示框"))
        self.pushButton.setText(_translate("MainWindow", "消息框"))
        self.pushButton_2.setText(_translate("MainWindow", "警告框"))
        self.pushButton_3.setText(_translate("MainWindow", "问题框"))
        self.pushButton_4.setText(_translate("MainWindow", "错误框"))
        self.pushButton_5.setText(_translate("MainWindow", "关于框"))
        # 关联“消息框”按钮的方法
        self.pushButton.clicked.connect(self.info)
        # 关联“警告框”按钮的方法
        self.pushButton_2.clicked.connect(self.warn)
        # 关联“问题框”按钮的方法
        self.pushButton_3.clicked.connect(self.question)
        # 关联“错误框”按钮的方法
        self.pushButton_4.clicked.connect(self.critical)
        # 关联“关于框”按钮的方法
        self.pushButton_5.clicked.connect(self.about)

    def info(self): # 显示消息提示框
        QMessageBox.information(None, '消息', '这是一个消息提示框', QMessageBox.Ok)

    def warn(self): # 显示警告提示框
        QMessageBox.warning(None, '警告', '这是一个警告提示框', QMessageBox.Ok)

    def question(self): # 显示问题提示框
        QMessageBox.question(None, '问题', '这是一个问题提示框', QMessageBox.Ok)

    def critical(self): # 显示错误提示框
        QMessageBox.critical(None, '错误', '这是一个错误提示框', QMessageBox.Ok)

    def about(self): # 显示关于提示框
        QMessageBox.about(None, '关于', '这是一个关于提示框')


# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程