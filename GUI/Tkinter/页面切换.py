# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-03 19:16
"""
import tkinter as tk


class Index(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(expand=1, fill="both")
        self.frame_left = tk.Frame(self)
        self.frame_left.pack(side='left', expand=1, fill="x", padx=5, pady=5)
        # 三个按钮用于切换页面
        for i in ["增加", "删除", "撤销"]:
            but = tk.Button(self.frame_left, text=i)
            but.pack(side='top', expand=1, fill="y")
            but.bind("<Button-1>", self.change)
            # 用于承载切换的页面内容
        self.frame_right = tk.Frame(self)
        self.frame_right.pack(side='left', expand=1, fill="both", padx=5, pady=5)

        lab = tk.Label(self.frame_right, text="我是第一个页面")
        lab.pack()

    # 根据鼠标左键单击事件，切换页面
    def change(self, event):
        res = event.widget["text"]
        for i in self.frame_right.winfo_children():
            i.destroy()
        if res == "增加":
            Page1(self.frame_right)
        elif res == "删除":
            Page2(self.frame_right)
        elif res == "撤销":
            Page3(self.frame_right)


class Page1(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(expand=1, fill="both")
        tk.Label(self, text="我是page1").pack()


class Page2(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(expand=1, fill="both")
        tk.Label(self, text="我是page2").pack()


class Page3(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(expand=1, fill="both")
        tk.Label(self, text="我是page3").pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("界面演示")
    index = Index(root)
    root.geometry('650x450+300+200')
    root.mainloop()
