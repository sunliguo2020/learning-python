# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-11-01 22:38
"""
import tkinter
from tkinter import ttk

root = tkinter.Tk()


def callbackFunc(event):
    print("New Element Selected")
    print(comboExample.current(), comboExample.get())


labelTop = tkinter.Label(root, text="选择网络")
labelTop.grid(column=2, row=0)

comboExample = ttk.Combobox(root,values=[
                                "January",
                                "February",
                                "March",
                                "April"])
print(dict(comboExample))

comboExample.grid(column=2, row=1)
comboExample.current(1)
comboExample.bind("<<ComboboxSelected>>", callbackFunc)

root.mainloop()
