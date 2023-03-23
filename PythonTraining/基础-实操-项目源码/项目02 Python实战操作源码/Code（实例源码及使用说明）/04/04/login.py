# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(320, 200)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.okbtn = QtWidgets.QPushButton(self.centralwidget)
        self.okbtn.setGeometry(QtCore.QRect(130, 150, 51, 23))
        self.okbtn.setObjectName("okbtn")
        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(199, 150, 51, 23))
        self.exitbtn.setObjectName("exitbtn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 261, 101))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 13, 51, 21))
        self.label.setObjectName("label")
        self.username = QtWidgets.QTextEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(70, 10, 181, 31))
        self.username.setObjectName("username")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 65, 48, 21))
        self.label_3.setObjectName("label_3")
        self.pwd = QtWidgets.QTextEdit(self.widget)
        self.pwd.setGeometry(QtCore.QRect(70, 60, 181, 31))
        self.pwd.setObjectName("pwd")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "用户登录"))
        self.okbtn.setText(_translate("LoginWindow", "登录"))
        self.exitbtn.setText(_translate("LoginWindow", "退出"))
        self.label.setText(_translate("LoginWindow", "用户名："))
        self.label_3.setText(_translate("LoginWindow", "密  码："))

