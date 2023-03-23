from tkinter import *
from tkinter.messagebox import *
import random
root = Tk()
gif=["验证码0","验证码1","验证码2","验证码3","验证码4","验证码5","验证码6","验证码7","验证码8","验证码9","验证码10","验证码11","验证码12"]
note=["36uad","eun2p","tqy19","1tt8i","1gria","4gsah","2q6gy","2gnf7","q4q1y","5qhi6","1ferh","wtyiq2","5ttyi"]
def setgif():
    global many
    global maxp
    global ranima
    global frames
    many = random.randint(0, len(gif) - 1)
    ranima = './cap/' + gif[many] + '.gif'

    maxp = 6
    frames = [PhotoImage(file=ranima, format='gif -index %i' % (i)) for i in range(maxp)]
    showp(0)


def showp(x):
    global maxp
    global frames
    frame = frames[x]
    x += 1
    label = Label(root, image=frame, height=23).grid(column=2, row=1)
    root.after(800, showp, x % maxp)


def dupass():
    global many
    if str(note[many]).lower() == m_str_var.get().strip("").lower():
        warn = showwarning(title='动态验证码', message='验证通过，将退出系统！')
        root.destroy()
    else:
        warn = showwarning(title='动态验证码', message='验证码不正确，请重新输入！')
        setgif()


def close():
    root.destroy()
root.title('动态验证码')
root.wm_attributes('-topmost', 1)
root.geometry('400x110')

image1 = PhotoImage(file='sport.png')
add = Label(root,text='新增会员',image=image1).grid(column=0, row=0)
explain = Label(root,text='请输入验证码：').grid(column=0, row=1)
m_str_var = StringVar()
cap=Entry(text='0',textvariable=m_str_var,width=10).grid(column=1, row=1)

actre = Button(root,text="换一张", relief=FLAT, command=setgif,width=10)      
actre.grid(column=3, row=1)

actis = Button(root, text="确认", command=dupass,width=10)      
actis.grid(column=2, row=2)
actend = Button(root, text="退出", command=close,width=10)      
actend.grid(column=3, row=2)
setgif()
root.mainloop()
