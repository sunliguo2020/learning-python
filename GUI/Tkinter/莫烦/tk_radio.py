# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/6 22:03
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=40, text='empty')
l.pack()


def print_selection():
    l.config(text='You have selected' + var.get())


r1 = tk.Radiobutton(window, text='OptionA',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='OptionB',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text='OptionC',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()

window.mainloop()
