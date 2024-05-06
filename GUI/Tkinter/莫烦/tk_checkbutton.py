# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/7 19:30
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python!')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++!')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')


var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
var2 = tk.IntVar()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
window.mainloop()
