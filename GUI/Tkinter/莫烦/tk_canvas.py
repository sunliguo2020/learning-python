# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/7 19:40
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')

canvas = tk.Canvas(window, bg='blue', height=400, width=400)
image_file = tk.PhotoImage(file='accessKeyCode.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)

canvas.pack()
window.mainloop()
