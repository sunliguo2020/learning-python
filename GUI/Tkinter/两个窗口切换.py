# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-03 19:10
"""
import tkinter as tk
from tkinter import *


class MyApp(object):

    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        btn = tk.Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()

    def hide(self):
        """"""
        self.root.withdraw()

    def openFrame(self):
        """"""
        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.geometry("400x300")
        otherFrame.title("otherFrame")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        btn = tk.Button(otherFrame, text="Close", command=handler)
        btn.pack()

    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()
