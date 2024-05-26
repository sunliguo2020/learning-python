# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/7 20:32
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')

tk.Label(window, text='on the window', bg='red', fg='white').pack()

frm = tk.Frame(window, bg='yellow', borderwidth=10)
frm.pack()

frm_l = tk.Frame(frm, bg='green', borderwidth=1, height=100)
frm_r = tk.Frame(frm)

frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l, text='on the frml1', bg='red', fg='white').pack()
tk.Label(frm_l, text='on the frml2', bg='red', fg='white').pack()
tk.Label(frm_r, text='on the frmr', bg='red', fg='white').pack()

window.mainloop()
