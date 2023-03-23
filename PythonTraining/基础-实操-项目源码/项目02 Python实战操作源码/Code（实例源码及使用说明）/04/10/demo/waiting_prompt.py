# *_* coding : UTF-8 *_*
# 文件名称   ：waiting_prompt.py
# 开发工具   ：PyCharm

from window import Ui_MainWindow                        # 导入窗体ui类
from PyQt5.QtWidgets import QMainWindow, QApplication   # 导入qt窗体类
from PyQt5 import QtGui                                 # 导入窗体ui类
import sys                                               # 导入系统模块
# 主窗体初始化类
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
    def start_loading(self):
        self.gif = QtGui.QMovie('loading.gif')  # 加载gif图片
        self.loading.setMovie(self.gif)         # 设置gif图片
        self.gif.start()                        # 启动图片，实现等待gif图片的显示
    def stop_loading(self):
        self.gif.stop()
        self.loading.clear()
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI对象
    main = Main()  # 创建主窗体ui类对象
    main.show()  # 显示主窗体
    main.pushButton_start.clicked.connect(main.start_loading)   # 启动加载提示框
    main.pushButton_stop.clicked.connect(main.stop_loading)     # 停止加载提示框
    sys.exit(app.exec_())  # 除非退出程序关闭窗体，否则一直运行
