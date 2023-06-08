# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-06 8:02
MAC  OS  Python3.6
用tkinter实现简单的布局，加上ping、time和logging模块测试连通性并生成log
"""

import logging
import os.path
import time
import tkinter as tk

# 主界面
window = tk.Tk()  # 窗口函数
window.title('window')  # 窗口的名字
window.geometry('400x400')  # 窗口的大小，x是字母

# IP显示label和entry
tk.Label(window, text="ip address:").grid(row=0)  # grid是布局，0表示放在第一行
ip = tk.Entry(window)  # 设置IP entry
ip.grid(row=0, column=1)  # 放在第一行，第一列

# port显示label和entry
tk.Label(window, text="port:").grid(row=1)  # 将port放在第二行
port = tk.Entry(window)  # 设置port entry
port.grid(row=1, column=1)  # 放在第二行，第一列

log_format = " %(asctime)s-%(name)s-%(levelname)s-%(message)s"  # log的格式设定
time_format = " %Y-%m-%d %H:%M:%S"  # 时间格式设定
logging.basicConfig(
    filename='test.log', level=logging.INFO, format=log_format, datefmt=time_format)  # log名字，等级设定，log默认生成在该py文件所在目录


# ping方法
def ping():
    print(ip.get())
    backinfo = os.system('ping ' + ip.get())  # 丢包5次
    print(backinfo)
    if backinfo == 0:  # 返回0为True
        showinfo("connect    ok")  # 显示在text中
        logging.info("connect    ok")  # 显示在log中
    else:
        showinfo("connect    fail")  # 显示在text中
        logging.info("connect    fail")  # 显示在log中


tk.Button(window, text="connect", font=('Arial', 10), command=ping).grid(row=0, column=2)
# 设置ping button，放在第一行，第二列

# 显示text定义
text = tk.Text(window, width=50, height=50)  # 设置高度和宽度
text.grid(row=2, column=1)


# 定义信息显示的方法
def showinfo(result):
    realtime = time.strftime("%Y-%m-%d %H:%M:%S ")
    textvar = realtime + result  # 系统时间和传入结果
    text.insert('end', textvar)  # 显示在text框里面
    text.insert('insert', '\n')  # 换行


# 定义清除方法
def clear():
    text.delete(0.0, tk.END)  # 清楚text中的内容，0.0为删除全部

    # 显示text
    text.place(x=100, y=150)  # place为布局，放在坐标为（100，150）的地方


# 点击方法定义
def hit(temp):
    if temp == "start":
        showinfo("start    testing")  # 显示在text中的内容
        showinfo("result is …")
        logging.info("program is running")  # 显示在log中的内容
    else:
        showinfo("stop        testing")  # 显示在text中的内容
        logging.info("program        stopped")  # 显示在log中的内容


tk.Button(window, text="Start", font=('Arial', 10), command=lambda: hit("start")).place(x=100, y=100)  # 设置开始button
tk.Button(window, text="Stop", font=('Arial', 10), command=lambda: hit("stop")).place(x=200, y=100)  # 设置停止button

clear_button = tk.Button(window, text='Clear', font=('Arial', 20), command=clear)  # 设置清除button
clear_button.place(x=300, y=100)  # 显示清除button

window.mainloop()  # 界面循环
