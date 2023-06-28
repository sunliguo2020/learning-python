# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-23 9:23
"""
from tkinter import *


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())


top = Tk()
top.geometry('250x150+100+100')

label = Label(top, text='Hello world!',
              font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=100, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit = Button(top, text='QUIT', command=top.quit,
              activeforeground='white',
              activebackground='red')
quit.pack()

top.mainloop()
