# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/7 19:20
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection(v):
    l.config(text='you have selected' + v)


s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200,
             showvalue=0, variable=None, tickinterval=3, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
