# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setBackgoundimage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
'''
  设置窗体背景图片，及自动适应窗体大小
'''
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QBrush,QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "使背景图片自动适应窗体大小"))
        self.pushButton.setText(_translate("MainWindow", "选择图片"))
        # 关联“加载图片”按钮的方法
        self.pushButton.clicked.connect(self.setImg)


    # 选择背景图片
    def setImg(self):
        try:
            # waterimg即为选择的背景图片，第二形参为对话框标题，第三个为对话框打开后默认的路径
            self.waterimg = QFileDialog.getOpenFileName(None,'选择背景图片','C:\\',"图片文件(*.jpeg;*.png;*.jpg;*.bmp)")
            # 设置窗体背景
            palette = QtGui.QPalette()
            # 设置窗体背景自适应
            palette.setBrush(MainWindow.backgroundRole(), QBrush(
                QPixmap(self.waterimg[0]).scaled(MainWindow.size(), QtCore.Qt.IgnoreAspectRatio,
                                               QtCore.Qt.SmoothTransformation)))
            MainWindow.setPalette(palette)
            MainWindow.setAutoFillBackground(True)  # 设置自动填充背景
        except Exception as e:
            print(e)


# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程
