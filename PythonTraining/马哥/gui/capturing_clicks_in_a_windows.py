from tkinter import *

root = Tk()

def callback(event):
    print('clicked at',event.x,event.y)
    label.config(text=f'clicked at {event.x} {event.y}')

frame = Frame(root,width=200,height=200)

frame.bind('<Button-1>',callback)

frame.pack()

label = Label(root)
label.pack()
root.mainloop()