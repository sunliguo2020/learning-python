# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-20 7:18
"""
from tkinter import *

root =Tk()

li = ["C","Python",'php','html','sql','java']

movie = ['css','jQuery',"Bootstrap"]

# 创建两个列表组件
listb = Listbox(root)
listb2 = Listbox(root)

for item in li :
    listb.insert(0,item)
for item in movie :
    listb2.insert(0,item)
listb.pack()
listb2.pack()

root.mainloop()