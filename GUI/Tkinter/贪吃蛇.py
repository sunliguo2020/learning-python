# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/13 18:08
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import random
import tkinter as tk

count_add = 0
list_lld = []
dd_list = []

next_num = "right"
APP = tk.Tk()
APP.geometry("1000x600+200+200")
direction = 'right'
C = tk.Canvas(APP, width=1000, height=600, background="black")

x_ = random.randrange(0, 900, 20)
y_ = random.randrange(0, 580, 20)

l = tk.Label(C, font=("Arial", 16), text="分数:0")

o = C.create_rectangle(x_, y_, x_ + 20, y_ + 2, fill='#ffff00')


def create_o():
    x_ = random.randrange(0, 980, 20)
    y_ = random.randrange(0, 580, 20)
    o = C.create_rectangle(x_, y_, x_ + 20, y_ + 20, fill='#ffff00')
    return o


x, y, w, h = 20, 20, 40, 40
a = C.create_rectangle(x, y, w, h, fill='#ffffff')

list_lld.append(C.create_rectangle(x - 20, y, w - 20, h, fill='#ffffff'))
list_lld.append(C.create_rectangle(x - 40, y, w - 40, h, fill='#ffffff'))


def right(b, i):
    if i:
        C.coords(b, i)
    else:
        C.move(b, 20, 0)


def left(b, i):
    if i:
        C.coords(b, i)
    else:
        C.move(b, -20, 0)


def top(b, i):
    if i:
        C.coords(b, +i)
    else:
        C.move(b, 0, -20)


def down(b, i):
    if i:
        C.coords(b, i)
    else:
        C.move(b, 0, 20)


def if_post(stride_x, stride_y):
    stride_x = 0 if stride_x > 1000 else stride_x
    stride_y = 1000 if stride_x < 0 else stride_x

    stride_y = 0 if stride_y > 600 else stride_y
    stride_y = 600 if stride_y < 0 else stride_y

    return stride_x, stride_y, stride_x + 20, stride_y + 20


def get_fie():
    while True:
        tnds = False
        a_list = []
        check_add = False
        global list_lld
        global o
        global count_add
        global direction

        a_path = C.coords(a)
        stride_x, stride_y, stride_x1, stridey1 = C.coords(a)
        b_path = C.coords(o)
        [a_list.append(C.coords(i)) for i in list_lld]


APP.mainloop()
