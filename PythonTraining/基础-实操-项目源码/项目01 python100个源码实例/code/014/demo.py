from tkinter import *
from tkinter.messagebox import *
import time
import random
root=Tk()
rans=[0.1,0.08,0.06,0.04]
count=0
start=False
def ten():                                           # 游戏主题函数
    global start                                    # 定义全局变量start，记录游戏状态
    global count                                     # 定义全局变量count，记录秒数
    num=random.choice(rans)                         # 随机产生间隔时间，增加游戏难度
    fight['text']='停止'                            
    if not start:                                    # 如果是停止状态
        start=True
        while start:
            time.sleep(num)
            count+=0.2
            show['text']=format(count,'.1f')
            show.update()                             
        if show['text']==str(10.0):                # 如果等于10秒，即挑战成功
            warn=showwarning(title='挑战10秒', message='挑战成功，您消费可全部免单！')
        else:
            warn=showwarning(title='挑战10秒', message='挑战失败，可以领取代金券一张！')
    else:
        start=False
        fight['text']='继续挑战'
        count=0
root.title('挑战10秒')                                        #  设置窗体标题
root.wm_attributes('-topmost', 1)                            #  设置窗体置顶
root.geometry('200x80')                                       #  设置窗体大小
root.resizable(width=False, height=False)                   #  设置窗体尺寸不可改变
topic = Label(root, text='挑战10秒')                        #  设置窗体中游戏标题
topic.pack()
show=Label(root,text=str(count))
show.pack()
fight=Button(root,text='开始挑战',command=ten)
fight.pack()
mainloop()
