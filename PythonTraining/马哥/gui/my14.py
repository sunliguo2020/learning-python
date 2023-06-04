# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-04 14:06
"""

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__()

        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # <class 'tkinter.PhotoImage'>
        self.photos = [PhotoImage(file='imgs/puke/puke' + str(i + 1) + '.gif') for i in range(10)]
        # <class 'tkinter.Label'>
        self.pukes = [Label(self.master, image=self.photos[i]) for i in range(10)]

        print(type(self.photos[0]))
        print(type(self.pukes[0]))

        for i in range(10):
            self.pukes[i].place(x=10 + i * 40, y=50)
            # self.pukes[i].pack(side='left')

        # 为所有的Label增加事件处理
        self.pukes[0].bind_class("Label", "<Button-1>", self.chupai)

    def chupai(self, event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)


if __name__ == '__main__':
    root = Tk()
    root.geometry("550x300+200+300")
    root.title("纸牌游戏")

    app = Application(master=root)

    root.mainloop()
