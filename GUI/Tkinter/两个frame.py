# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-04 7:54
"""
import tkinter as tk

window = tk.Tk()
window.title('frame示例')       # 设置窗口的标题
window.geometry('200x200')     # 设置窗口的大小

# 在window上创建一个frame
frm = tk.Frame(window)
frm.pack()

# 在frm上创建两个frame， 一个在左，一个在右
frm_left = tk.Frame(frm)
frm_right = tk.Frame(frm)

frm_left.pack(side='left')      # 设置相对位置，一个在左，一个在右
frm_right.pack(side='right')

# 创建两个label，一个放在frm_left上，一个放在frm_right上
tk.Label(frm_left, text='在左侧').pack()
tk.Label(frm_right, text='在右侧').pack()

window.mainloop()