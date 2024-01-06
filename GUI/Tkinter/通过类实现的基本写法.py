# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-04 7:40
"""
from tkinter import *


class application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas = Canvas(self, width=200, height=200, bg='green')
        self.canvas.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x300')
    app = application(root)
    root.mainloop()
