# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/7 19:52
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')

l = tk.Label(window, text='', bg='red', fg='white')
l.pack()

counter = 0


def do_job():
    global counter
    l.config(text='do' + str(counter))
    counter += 1


menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label="New", command=do_job)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)

editmenu.add_command(label="Cut", command=do_job)

window.config(menu=menubar)
window.mainloop()
