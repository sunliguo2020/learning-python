# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/17 22:31
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from tkinter import *

from PIL import Image, ImageTk


class Window(Frame):
    """

    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open('parrot.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry('400x300')
root.mainloop()
