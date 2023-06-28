# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-20 17:12
"""
import threading
import time
from random import randint
from tkinter import *

# Initialize a new window
root = Tk()
root.geometry('500x400')


# A function that interrupts for five seconds
def five_seconds():
    # label.config(text="five_seconds 开始了！")
    time.sleep(2)
    label.config(text=f'5 seconds up!{randint(1, 100)}')


# A function that generates a random number
def random_numbers():
    rand_label.config(text=f'The random number is: {randint(1, 100)}')


label = Label(root, text='Hello there!')
label.pack(pady=20)
# A button that calls a function
# 不使用线程
# button1 = Button(root, text='5 seconds', command=five_seconds)
# button1 = Button(root, text='5 seconds', command=threading.Thread(target=five_seconds).start())
# 使用 lambda 线程

button1 = Button(root, text='5 seconds', command=lambda:threading.Thread(target=five_seconds).start())
button1.pack(pady=20)

button2 = Button(root, text='pick a random number', command=lambda: random_numbers())
button2.pack(pady=20)
rand_label = Label(root, text='')
rand_label.pack(pady=20)
root.mainloop()
