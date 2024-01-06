# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-03 21:29
"""
from tkinter import *


def callback():
    print(f'la1原来的值为:{la1}')
    la1.config(text="设置文本")  # 通过config方法来再设置标签文本


root = Tk()
la1 = Label(root, text='初始文本')  # 通过text属性来设置标签文本
la1.pack()

but_set = Button(root, text="设 置", command=callback)  # command参数来调用函数
but_set.pack(pady=10)

root.mainloop()
