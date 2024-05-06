import tkinter as tk
from tkinter import messagebox


def mouseTest(a, b):
    messagebox.showinfo('结果', f"传递的参数是a={a},b={b}")


root = tk.Tk()
# tk.Button(root,text='测试',command = lambda:mouseTest("s","z")).pack()
tk.Button(root, text='测试', command=mouseTest("s", "z")).pack()
root.mainloop()
