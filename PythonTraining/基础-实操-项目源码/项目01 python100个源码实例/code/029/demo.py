from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
plt.rcParams['font.sans-serif'] = ['SimHei']	# 显示中文
plt.rcParams['axes.unicode_minus'] = False		# 显示负号
df = pd.read_excel('./data/employee_data.xlsx')
main = Tk()
main.title('员工满意度调查数据分析')#设置标题栏
#设置窗口的大小
main.geometry('800x560')
main.iconbitmap('./images/mr.ico')   #窗体图标
#生成主界面
frame= tk.Frame()
frame.grid(row=0, column=0,padx=1,pady=1)
#添加背景图片
imgInfo = PhotoImage(file = './images/bg2.png')
lblImage = Label(frame, image = imgInfo)
lblImage.grid()
#显示图表
def chart_view(f1):
    img_open = Image.open(f1)
    img = ImageTk.PhotoImage(img_open)
    chart_preview.config(image=img)
    chart_preview.image = img
    main.update_idletasks()   #更新图片，必须update
    chart_preview.place(x = 230, y = 120)  #图表位置
    
def chart1():
  f1='mr01.png'
  #总体情况分析(饼形图)很满意、满意等各多少项，所占百分比
  df1=df.groupby(['调查内容','满意度'])['员工匿名'].count().reset_index()
  a_df=df1[df1['满意度']=='很满意']
  b_df=df1[df1['满意度']=='满意']
  c_df=df1[df1['满意度']=='基本满意']
  d_df=df1[df1['满意度']=='不太满意']
  e_df=df1[df1['满意度']=='不满意']
  a=len(list(a_df['调查内容']))
  b=len(list(b_df['调查内容']))
  c=len(list(c_df['调查内容']))
  d=len(list(d_df['调查内容']))
  e=len(list(e_df['调查内容']))
  plt.figure(figsize=(9,7)) #调节图形大小
  labels = ['很满意','满意','基本满意','不太满意','不满意'] #定义标签
  sizes = [a,b,c,d,e] #设置饼形图每块的值
  colors = ['red', 'yellow', 'slateblue', 'green','magenta'] #设置饼形图每块的颜色
  patches, l_text, p_text = plt.pie(sizes, #绘图数据
        labels=labels,#添加区域水平标签
        colors=colors,# 设置饼图的自定义填充色
        labeldistance=1.02,#设置各扇形标签（图例）与圆心的距离
        autopct='%.1f%%',# 设置百分比的格式，这里保留一位小数
        startangle=90,# 设置饼图的初始角度
        radius = 0.5, # 设置饼图的半径
        center = (0.2,0.2), # 设置饼图的原点
        textprops = {'fontsize':14, 'color':'k'}, # 设置文本标签的属性值
        pctdistance=0.6)# 设置百分比标签与圆心的距离
  # 设置x，y轴刻度一致，这样饼图才能是圆的
  plt.axis('equal')
  #显示图例
  plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 0.8))
  plt.grid()
  plt.savefig('mr01.png',dpi=60)
  chart_view(f1)

def chart2():
  f1='mr02.png'
  df['很满意'] = df.apply(lambda row: 1 if row['满意度']=='很满意'else 0, axis=1)
  df['满意'] = df.apply(lambda row: 1 if row['满意度']=='满意'else 0, axis=1)
  df['基本满意'] = df.apply(lambda row: 1 if row['满意度']=='基本满意'else 0, axis=1)
  df['不太满意'] = df.apply(lambda row: 1 if row['满意度']=='不太满意'else 0, axis=1)
  df['不满意'] = df.apply(lambda row: 1 if row['满意度']=='不满意'else 0, axis=1)
  df1 = df.groupby(['调查内容'])['很满意','满意','基本满意','不太满意','不满意'].sum().reset_index()
  #某一项的满意率=（很满意人数*100+满意人数*80+基本满意人数*60+不太满意人数*30+不满意人数*0）/总人数
  df3=(df1['很满意']*100+df1['满意']*80+df1['基本满意']*60+df1['不太满意']*30+df1['不满意']*0)/8
  name_list =df1['调查内容'].values.tolist()
  num_list=df3.values.tolist()
  f, ax = plt.subplots(figsize=(7,5))#调节图表大小
  #画横向水平条形图
  plt.barh(name_list, num_list,color='dodgerblue')
  plt.xticks(fontsize = 8)
  plt.yticks(fontsize = 8)
  plt.subplots_adjust(left=0.5, wspace=0.35, hspace=0.25,
                    bottom=0.13, top=0.91)
  #横向水平条形图加百分比标注
  for y, x in enumerate(df3):
    plt.text(x+0.2, y-0.3, "%.f%%" %x,family='simhei',fontsize=11)
  f.savefig('mr02.png',dpi=80)
  chart_view(f1)
def chart3():
  f1='mr03.png'
  df['很满意'] = df.apply(lambda row: 1 if row['满意度']=='很满意'else 0, axis=1)
  df['满意'] = df.apply(lambda row: 1 if row['满意度']=='满意'else 0, axis=1)
  df['基本满意'] = df.apply(lambda row: 1 if row['满意度']=='基本满意'else 0, axis=1)
  df['不太满意'] = df.apply(lambda row: 1 if row['满意度']=='不太满意'else 0, axis=1)
  df['不满意'] = df.apply(lambda row: 1 if row['满意度']=='不满意'else 0, axis=1)
  df1 = df.groupby(['类别'])['很满意','满意','基本满意','不太满意','不满意'].sum().reset_index()
  #某一项的满意率=（很满意人数*100+满意人数*80+基本满意人数*60+不太满意人数*30+不满意人数*0）/总人数
  num1=df1['类别']
  df3=(df1['很满意']*100+df1['满意']*80+df1['基本满意']*60+df1['不太满意']*30+df1['不满意']*0)/(df1['很满意']+df1['满意']+df1['基本满意']+df1['不太满意']+df1['不满意'])
  print(df3)
  labels = np.array(df1['类别']) # 标签
  dataLenth = 4  # 数据长度
  data_radar = np.array(df3) # 数据
  angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)  # 分割圆周长
  data_radar = np.concatenate((data_radar, [data_radar[0]]))  # 闭合
  angles = np.concatenate((angles, [angles[0]]))  # 闭合
  plt.figure(figsize=(6,5)) #调节图形大小
  plt.polar(angles, data_radar, 'bo-', linewidth=1)  # 极坐标系
  plt.thetagrids(angles * 180/np.pi, labels)  # 标签
  plt.fill(angles, data_radar, facecolor='r', alpha=0.25)# 填充
  plt.ylim(0, 100)  #设置显示的极径范围
  plt.savefig('mr03.png',dpi=80)
  chart_view(f1)
def close():
  main.destroy()  #关闭tkinter窗口destroy()方法
#添加命令按钮
button1=tk.Button(frame,width=20,text='总体满意度分析',command=chart1).place(x=30, y=210)
button2=tk.Button(frame,width=20,text='各项内容满意度分析',command=chart2).place(x=30, y=260)
button3=tk.Button(frame,width=20,text='维度分析',command=chart3).place(x=30, y=310)
button4=tk.Button(main,width=20,text='退出',command=close).place(x=30, y=360)
#添加显示图表的Label
chart_preview=tk.Label(main)
# 主窗口循环显示
main.mainloop()
main.update()

