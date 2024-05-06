# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/6 21:41
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()
window.title = ''
window.geometry('400x400')

e = tk.Entry(window, show='*', )
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


b1 = tk.Button(window, text='insert point', width=15,
               height=2, command=insert_point)
b1.pack()


def insert_end():
    var = e.get()
    t.insert('end', var)


b2 = tk.Button(window, text='insert end', width=15,
               height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()
window.mainloop()
