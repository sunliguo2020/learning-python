# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-04 12:57
"""
import random
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__()

        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas = Canvas(self, width=300, height=200, bg='green')
        self.canvas.pack()

        line = self.canvas.create_line(10, 10, 30, 20, 40, 50)
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        oval = self.canvas.create_oval(50, 50, 100, 100)

        global photo
        photo = PhotoImage(file='img/ads.png')
        self.canvas.create_image(150, 170, image=photo)

        Button(self, text='画10个矩形', command=self.draw50Recg).pack(side='left')

    def draw50Recg(self):
        for i in range(1000):
            x1 = random.randrange(int(self.canvas['width']) / 2)
            y1 = random.randrange(int(self.canvas['height']) / 2)

            x2 = x1 + random.randrange(int(self.canvas['width']) / 2)
            y2 = y1 + random.randrange(int(self.canvas['height']) / 2)

            self.canvas.create_rectangle(x1, y1, x2, y2)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+200+300")
    root.title("一个canvas的测试")

    app = Application(master=root)

    root.mainloop()
