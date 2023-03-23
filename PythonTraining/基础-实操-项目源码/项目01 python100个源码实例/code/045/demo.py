import tkinter as tk
import time
import threading
import random
#建立主窗口window
window = tk.Tk()
#设置窗口标题栏名称
window.title('轻松背单词')
#设置窗口的大小
window.geometry('640x765')
#标记窗体是否运行
window.flag = True
#设置label背景为图片
image_file = tk.PhotoImage(file='bg.png')
label1 = tk.Label(window,text='',font = ("黑体", 60,"normal"),compound = 'center',image=image_file)
label2 = tk.Label(window,text='',font = ("黑体", 15,"normal"))
label1.pack()
label2.place(x=230,y=430)
words=[]
#读取文本（单词本）
f = open('words.txt', 'r',encoding='utf-8')
for s in f.readlines():
   words.append(s)
#定义自动切换单词的方法
def autoChange():
    window.flag=True
    while window.flag:
        i=random.randint(0, len(words)-1)  #随机显示单词
        a=words[i].split()                 #文本分割为列表
        b1=a[0:1]                          #第1列单词
        b2=a[2:4]                          #第2、3列音标和解释
        #label组件显示文本
        label1['text']=b1
        label2['text']=b2
        time.sleep(3)
#用线程控制自动切换单词
t = threading.Thread(target=autoChange)
t.start()
window.mainloop()
window.flag=False
