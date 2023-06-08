# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-08 16:10
"""
from tkinter import *
from tkinter import filedialog

import win32api

root = Tk()

root.title('Print Hard Copies')
root.geometry('200x200')


#  Print File Function
def print_file():
    # Ask for (which you want to print)
    file_to_print = filedialog.askopenfilename(
        initialdir="/", title='Select file',
        filetypes=(("text files", "*.txt"), ("all files", "*.*"))
    )
    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, '.', 0)


Button(root, text="Print File", command=print_file).pack()

root.mainloop()
