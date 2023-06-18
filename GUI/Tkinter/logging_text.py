# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-20 8:03
logging自带的handler有很多类型，StreamHandler、FileHandler、RotatingFileHandler、TimedRotatingFileHandler、NullHandler、WatchedFileHandler、SocketHandler、DatagramHandler、SysLogHandler、NtEventHandler、SMTPHandler、MemoryHandler、HTTPHandler

我想在GUI界面上显示日志内容，以上Handler都不支持。想到了两个思路，最后实现都成功了，而且很简单。

思路一：以tk.Text为父类创建一个新的类，增加相关的功能以适配 StreamHandler。在创建StreamHandler时作为参数传入。

实现：参考sys.stdou，因为StreamHandler(stream) 常规用法是把sys.stdout作为参数传进去的，查看StreamHandler源码见到其实就是在里面调用了sys.stdout的write()方法，即相当于print()。给新的类添加write()方法就可以了

思路二：构造一个新的Handler类，可以支持直接把tk.Text控件作为参数传入。

查了一下，发现各种handler最核心就是里面的 def emit(self, record) 这个函数，它确定了在哪里输出。重写emit函数即可。

"""

import datetime
import logging
import tkinter as tk


# 方案一
class LoggerBox(tk.Text):

    def write(self, message):
        self.insert("end", message)


# 方案二
class TextboxHandler(logging.Handler):
    def __init__(self, textbox):
        logging.Handler.__init__(self)
        self.textbox = textbox

    def emit(self, record):
        msg = self.format(record)
        self.textbox.insert("end", msg + "\n")


class App:
    def __init__(self, root):
        root.title("TextBox logger")
        root.geometry("600x300")

        tk.Button(root, text="Button", command=self.btn_command).place(x=150, y=40, width=70, height=25)

        # 方案一
        streamHandlerBox = LoggerBox(root, width=50, height=5)
        streamHandlerBox.place(x=40, y=70)
        self.log1 = logging.getLogger('log1')
        self.log1.setLevel(logging.INFO)
        handler = logging.StreamHandler(streamHandlerBox)
        self.log1.addHandler(handler)

        # 方案二
        normalTextBox = tk.Text(root, width=50, height=5)
        normalTextBox.place(x=40, y=200)
        self.log2 = logging.getLogger('log2')
        self.log2.setLevel(logging.INFO)
        handler = TextboxHandler(normalTextBox)
        self.log2.addHandler(handler)

    def btn_command(self):
        now = datetime.datetime.now()
        self.log1.info(f"LoggerBox:{now}")
        self.log2.info(f"TextboxHandler:{now}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
