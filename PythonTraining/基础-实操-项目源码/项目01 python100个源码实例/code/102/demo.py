
from tkinter import *
from tkinter.messagebox import *
import time
import os
root = Tk()
import random
dirall=[]
randima =[]

def call():
    global  image1
    global  image2
    global  image3
    global  image4
    global  image5
    global  selone
    global  seltwo
    dirall.clear()
    randima.clear()
    for dirs in os.walk('./test/'):
        dirall.append(dirs)
    secdir=dirall[0][1]
    luckima=random.choice(secdir)
    secdir.remove(luckima)
    decdir=luckima
    filelist=os.listdir('./test/'+decdir)
    selone = random.choice(filelist)
    randima.append(decdir+'/'+selone)
    filelist.remove(selone)
    seltwo =  random.choice(filelist)
    randima.append(decdir+'/'+seltwo)
    for i in range(3):
       randdir=random.choice(secdir)
       randfile=os.listdir('./test/'+randdir)
       randima.append(randdir+'/'+random.choice(randfile))
       secdir.remove(randdir)
    random.shuffle(randima)
 
    title=Label(root, text="所有的"+luckima).grid(column=1, row=0) 
    image1 = PhotoImage(file='test/'+randima[0])
    image2 = PhotoImage(file='test/'+randima[1])
    image3 = PhotoImage(file='test/'+randima[2])
    image4 = PhotoImage(file='test/'+randima[3])
    image5 = PhotoImage(file='test/'+randima[4])
    label = Label(root,image=image1).grid(column=0, row=1) 
    labe2 = Label(root,image=image2).grid(column=1, row=1) 
    labe3 = Label(root,image=image3).grid(column=2, row=1) 
    labe4 = Label(root,image=image4).grid(column=3, row=1) 
    labe5 = Label(root,image=image5).grid(column=4, row=1) 
def defcheck():
    cvar1.set(0)
    cvar2.set(0)
    cvar3.set(0)
    cvar4.set(0)
    cvar5.set(0)
def test():
    count=0
    if cvar1.get()==1:
        if selone not in randima[0] and seltwo not in randima[0]:
            warn=showwarning(title='图形验证码', message ='验证失败，请重新验证！' )
            count=20            
            call()
        else:
            count +=1
    if cvar2.get()==1 and count!=20:
        if selone not in randima[1] and seltwo not in randima[1]:
            warn=showwarning(title='图形验证码', message ='验证失败，请重新验证！' )
            count=20
            call()
        else:
            count+=1
    if cvar3.get()==1 and count!=20:
        if selone not in randima[2] and seltwo not in randima[2]:
            warn=showwarning(title='图形验证码', message ='验证失败，请重新验证！' )
            count=20
            call()
        else:
            count+=1
    if cvar4.get()==1 and count!=20:
        if selone not in randima[3] and seltwo not in randima[3]:
            warn=showwarning(title='图形验证码', message ='验证失败，请重新验证！' )
            count=20
            call()
        else:
            count +=1

    if cvar5.get()==1 and count!=20:
        if selone not in randima[4] and seltwo not in randima[4]:
            warn=showwarning(title='图形验证码', message ='验证失败，请重新验证！' )
            count=20
            call()
        else:
            count +=1
    if count==2 :
        mess=showwarning(title='图形验证码', message ='验证通过，将进入系统！' )
        root.destroy()  
    elif count==0:
        mess=showwarning(title='图形验证码', message ='请选择图形再验证！' )
    else:
        defcheck()
            
root.title('图形验证码')
root.wm_attributes('-topmost', 1)
root.geometry('500x180')
title=Label(root, text="请点击下面图中").grid(column=0, row=0)

call()



cvar1 = IntVar()
cvar2 = IntVar()
cvar3 = IntVar()
cvar4 = IntVar()
cvar5 = IntVar()
check1 = Checkbutton(root, text = "选择", variable = cvar1, onvalue = 1, offvalue = 0).grid(column=0, row=2) 
check2= Checkbutton(root, text = "选择", variable = cvar2,onvalue = 1, offvalue = 0).grid(column=1, row=2) 
check3 = Checkbutton(root, text = "选择", variable = cvar3, onvalue = 1, offvalue = 0).grid(column=2, row=2) 
check4= Checkbutton(root, text = "选择", variable = cvar4,onvalue = 1, offvalue = 0).grid(column=3, row=2)
check5 = Checkbutton(root, text = "选择", variable = cvar5, onvalue = 1, offvalue = 0).grid(column=4, row=2)
actis = Button(root, text="确认", command=test,width=8)      
actis.grid(column=3, row=3)    
actcal = Button(root, text="换一组", command=call,width=8)      
actcal.grid(column=4, row=3)   
root.mainloop()
