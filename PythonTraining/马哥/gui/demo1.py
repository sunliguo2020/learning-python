from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('我的第一个GUI程序')

root.geometry("500x300+100+200")

btn01 = Button(root)

btn01['text'] = "点我就送花"
# 我又做了修改
btn01.config(text='我又修改了!')
btn01.pack()


def songhua(e):
    messagebox.showinfo('Message', "送你一朵玫瑰花")
    print("送你99朵玫瑰花")


btn01.bind('<Button-1>', songhua)

root.mainloop()  # 调用组件的mainloop()方法，进入事件循环
