# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-20 8:03
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
