# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/6 21:51
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()
window.geometry('400x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())
    print(value)
    var1.set(value)


b1 = tk.Button(window, text='print selection', width=15,
               height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))

lb = tk.Listbox(window, listvariable=var2)
lb.insert('end', 'last')
lb.pack()
window.mainloop()
