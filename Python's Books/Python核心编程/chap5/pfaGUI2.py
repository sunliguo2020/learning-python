# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-23 10:04
"""
from functools import partial as pto
from tkinter import Tk, Button, X

from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
RECU = 'recu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': RECU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': RECU
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', "Warning Button Pressed!"
                             )
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top, text="QUIT", command=top.quit,
       bg='red', fg='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod')
RecuButton = pto(MyButton, command=infoCB, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)' % \
          (signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()'
           )
    eval(cmd)

top.mainloop()
