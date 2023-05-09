# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-08 18:43
"""
from tkinter import *

clock = Tk()
clock.title("it项目实例网 闹钟")  # 设置窗口的title
clock.geometry("800x200")  # 设置窗口的宽度与高度

add_time = Label(clock, text="时  分   秒", font=60).place(x=110)
clock.mainloop()  # 程序的主循环，像检测按钮的点击等都在这里进行操作
