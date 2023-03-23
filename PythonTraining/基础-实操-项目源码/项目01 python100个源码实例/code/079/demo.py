import csv
import tkinter as tk
import tkinter.messagebox
import datetime
import pandas as pd
import os
dt = datetime.datetime.now()
time = dt.strftime("%Y-%m-%d %H:%M:%S")
#保存参与抽奖的数据
def save():
  global num1
  #判断文件是否存在
  flag = os.path.isfile('./data/bwc_data.csv')
  if flag:
     #打开文件
     with open('./data/bwc_data.csv', 'r',newline='') as f:
             #读取数据
             reader = csv.reader(f)
             h1=next(reader)
             myval=[]
             for row in reader:
                #将“幸运码”列保存到myval列表中
                myval.append(int(row[3]))
                num1=max(myval)+1
     with open('./data/bwc_data.csv', 'a+',newline='') as f:
            writer=csv.writer(f)
            writer.writerow([txt_name.get(),txt_tel.get(),time,num1])   # 写入一行数据    
  else:
        num1=1000001
        with open('./data/bwc_data.csv', 'w',newline='') as f:# 如不指定newline='',有时会写入空行
            writer = csv.writer(f)
            writer.writerow(['姓名', '手机号', '参与抽奖时间','幸运码'])  # 写入一行标题
            writer.writerow([txt_name.get(),txt_tel.get(),time,num1])     # 写入第一行数据
  tkinter.messagebox.showinfo("消息提示",'您的幸运码是：'+str(num1))      #弹出消息提示框
#读取数据抽取幸运码
def read():
  aa ='./data/bwc_data.csv'
  df = pd.DataFrame(pd.read_csv(aa,encoding = 'gbk'))
  count=df.shape[0]  #参与人数
  df1=df.sort_values(by='幸运码',ascending=False).head(10)  #取最后10条记录
  print(df1)
  df2=pd.to_datetime(df1['参与抽奖时间'])
  print(df2)
  #幸运码算法
  sum1=0
  for i in df2:
      myval=int(i.timestamp())  #将参与抽奖时间转换为时间戳
      print(myval)
      sum1=sum1+myval           #时间戳求和
  print(sum1)
  w_num=sum1%count+1000001       #时间戳总和与人数取余加上第1位幸运码
  tkinter.messagebox.showinfo("消息提示",'获奖幸运码：'+str(w_num)+'、'+str(w_num+1)+'、'+str(w_num+2))      #弹出消息提示框
#建立主窗口window
window = tk.Tk()
#设置窗口标题栏名称
window.title('霸王餐抽奖')
#设置窗口的大小
window.geometry('600x390')
canvas = tk.Canvas(window, width=600, height=400)
image_file = tk.PhotoImage(file='./images/bg3.png')
image = canvas.create_image(320, 0, anchor='n', image=image_file)
canvas.pack(side='top')
# 在主窗口添加标签
l1 = tk.Label(window, text='姓    名：', font=('Arial', 12)).place(x=30, y=320)
l2=tk.Label(window, text='手机号：',font=('Arial', 12)).place(x=30, y=350)
# 在主窗口添加文本框
txt_name = tk.StringVar()
text1 = tk.Entry(window,textvariable=txt_name, show = None,width=45)
txt_tel= tk.StringVar()
text2 = tk.Entry(window,textvariable=txt_tel,show = None,width=45)
text1.place(x=100,y=320)
text2.place(x=100,y=350)
# 在主窗口添加命令按钮
button1 = tk.Button(window,width=10, height=3,text='点击参与',bg='tomato',command=save).place(x=430, y=310)
button2 = tk.Button(window,width=10, height=3,text='开奖',bg='orange',command=read).place(x=510, y=310)
# 主窗口循环显示
window.mainloop()



