# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-23 9:17
"""
import tkinter

top = tkinter.Tk()
quit = tkinter.Button(top, text='hello world', command=top.quit)

quit.pack()
top.mainloop()
