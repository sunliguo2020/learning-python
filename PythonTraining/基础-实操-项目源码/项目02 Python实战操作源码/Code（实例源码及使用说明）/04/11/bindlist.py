# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bindlist.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
'''
  对QListWidget列表进行数据绑定
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 190)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 401, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "对QListWidget列表进行数据绑定"))

        from collections import OrderedDict
        # 定义有序字典，作为List列表的数据源
        dict=OrderedDict({'诸葛维奇':'格雷格·波波维奇','石佛':'蒂姆·邓肯','妖刀':'马努·吉诺比利',
                          '法国跑车':'托尼·帕克','海军上将':'大卫·罗宾逊','冰人':'乔治·格文',
                          '三叔':'布鲁斯·鲍文','小将军':'埃弗里·约翰逊','超人':'肖恩·埃利奥特'})
        for key,value in dict.items():# 遍历字典，并分别获取到键值
            self.item = QtWidgets.QListWidgetItem(self.listWidget)# 创建列表项
            self.item.setText(key+'——'+value) # 设置项文本
            self.item.setToolTip(value)  # 设置提示文字

# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程