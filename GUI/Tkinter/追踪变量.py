# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-03 21:38
"""
from tkinter import *


def callback_r(*args):
    print('警告，变量被读取')  # 提醒变量被读取


def get():
    print(var.get())  # 输出读取的变量数据


root = Tk()

var = StringVar()  # 建立变量var为字符串变量
var.set('初始文本')  # 设置变量

en1 = Entry(root, textvariable=var)  # 通过textvariable=var将变量与文本绑定在一起
en1.pack()

var.trace('r', callback_r)  # trace追踪变量r模式，回调函数callback_r

but1 = Button(root, text="读 取", command=get)
but1.pack()

root.mainloop()