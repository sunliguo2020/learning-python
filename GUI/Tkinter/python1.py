# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/6 21:18
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('400x100')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, fg='red', bg='blue', font=('Arial', 12),
             width=15, height=2)
l.pack()
on_hit = False


def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('You hit me!')
    else:
        var.set('')
        on_hit = False
    l.config(text='Hit me!')


b = tk.Button(window, text='hit me!', width=15, height=2, command=hit_me)
b.pack()

window.mainloop()
