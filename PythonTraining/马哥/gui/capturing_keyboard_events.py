from tkinter import *

root = Tk()

def key(event):
    print('pressed',repr(event.char))
def callback(event):
    print('clicked at',event.x,event.y)
    label.config(text=f'clicked at {event.x} {event.y} {label.config}')
    print(frame.config())

frame = Frame(root,width=200,height=200)
frame.bind("<Key>",key)
frame.bind('<Button-1>',callback)

frame.pack()

label = Label(root)
label.pack()
root.mainloop()