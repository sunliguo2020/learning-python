# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-23 9:19
"""
import tkinter

top = tkinter.Tk()

hello = tkinter.Label(top, text="hello world")
hello.pack()

quit = tkinter.Button(top, text='QUIT',
                      command=top.quit, bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()
