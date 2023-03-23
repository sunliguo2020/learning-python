# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bindtable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
'''
  对QTableWidget表格进行数据绑定
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 501, 270))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0, 180)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "对QTableWidget表格进行数据绑定"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件大小"))
        self.pushButton.setText(_translate("MainWindow", "选择路径"))
        self.pushButton.clicked.connect(self.bindTable) # 关联“选择路径”的单击事件

    # 选择路径，并获取其中的所有文件信息显示在表格中
    def bindTable(self):
        try:
            import os
            # dir_path即为选择的文件夹的绝对路径，第二形参为对话框标题，第三个为对话框打开后默认的路径
            self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", os.getcwd())
            self.list = os.listdir(self.dir_path)  # 列出文件夹下所有的目录与文件
            flag=0 # 标识插入新行的位置
            for i in range(0, len(self.list)):  # 遍历文件列表
                # 拼接路径和文件名
                filepath = os.path.join(self.dir_path, self.list[i])
                if os.path.isfile(filepath): # 判断是否为文件
                    self.tableWidget.insertRow(flag)  # 添加新行
                    # 设置第一列的值为文件（夹）名
                    self.tableWidget.setItem(flag, 0, QtWidgets.QTableWidgetItem(self.list[i]))
                    fileinfo=os.stat(filepath) # 获取文件信息
                    # 设置第二列的值为文件大小
                    self.tableWidget.setItem(flag, 1, QtWidgets.QTableWidgetItem(str(fileinfo.st_size)+' B'))
                    flag+=1 # 计算下一个新行插入位置
        except Exception as e:
            print(e)


# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程