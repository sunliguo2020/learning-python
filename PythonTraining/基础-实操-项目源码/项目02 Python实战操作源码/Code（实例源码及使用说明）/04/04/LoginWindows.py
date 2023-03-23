# _*_ coding:utf-8   _*_
# 文件名称：LoginWindows.py
# 开发工具：PyCharm

import sys  # 导入操作系统模块

from PyQt5.QtCore import QCoreApplication  # 导入PyQt5的QtCore模块
from PyQt5.QtWidgets import QApplication,QMainWindow  # 导入PyQt5的QtWidgets模块
from login import *  # 导入登录窗体的UI类

# 登录窗体初始化类
class LoginWindows(QMainWindow,Ui_LoginWindow):
    def __init__(self): # 构造方法
        super(LoginWindows,self).__init__()  # 运行父类的构造方法
        self.setupUi(self) # 把自己作为参数传递给setupUi()方法
        self.exitbtn.clicked.connect(self.executeClick)  # 为退出按钮绑定槽函数

    def executeClick(self):  #退出按钮的自定义方法
        QCoreApplication.instance().quit()  # 关闭登录窗体
# 主程序入口
if __name__ == "__main__":
    app = QApplication (sys.argv) # 创建GUI对象
    login = LoginWindows() # 创建窗体UI类对象
    login.show()    # 显示窗体
    sys.exit(app.exec_())  # 除非退出程序关闭窗体，否则一直运行
