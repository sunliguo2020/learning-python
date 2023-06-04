# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-04 11:36
测试一个经典的GUI程序的写法，使用面向对象的方式
"""

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text='我是label', bg='black', fg='white', width=10, border=2)
        self.label01.pack()

        self.photo = PhotoImage(file='img/ads.png')
        self.label04 = Label(self, image=self.photo)
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个label的测试")

    app = Application(master=root)

    root.mainloop()
