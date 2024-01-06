# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-03 21:35
"""
from tkinter import *


def callback():
    var.set('再设置文本')  # 通过变量set方法来再设置文本


root = Tk()

var = StringVar()  # 建立变量var为字符串变量
var.set('初始文本')  # 设置变量

la1 = Label(root, textvariable=var)  # 将变量var跟文本绑定在一起
la1.pack()

but_set = Button(root, text="设 置", command=callback)  # command参数来调用函数
but_set.pack(pady=10)

root.mainloop()