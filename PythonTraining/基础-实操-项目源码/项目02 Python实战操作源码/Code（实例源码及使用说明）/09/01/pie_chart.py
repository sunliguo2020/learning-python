#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
aa ='../data/TB2018.xlsx'
df = pd.DataFrame(pd.read_excel(aa))
series=df['收货地址'].str.split(' ',expand=True)
df['省']=series[0]
df1=df.groupby(['省'],as_index=False)["买家实际支付金额"].sum().reset_index()
print(df1)
#降序排序
df1 = df1.sort_values(['买家实际支付金额'], ascending=False)
df1=df1.head(10)  #读取前10行
print(df1)
#区域饼形图
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.figure(figsize=(6,9)) #调节图形大小

labels = df1['省'].values.tolist() #定义标签
sizes = df1['买家实际支付金额'].values.tolist() #设置饼形图每块的值
colors = ['red', 'yellow', 'slateblue', 'green','magenta','cyan','darkorange','lawngreen','pink','gold'] #设置饼形图每块的颜色
plt.pie(sizes, #绘图数据
        labels=labels,#添加区域水平标签
        colors=colors,# 设置饼图的自定义填充色
        labeldistance=1.02,#设置各扇形标签（图例）与圆心的距离
        autopct='%.1f%%',# 设置百分比的格式，这里保留一位小数
        startangle=90,# 设置饼图的初始角度
        radius = 0.5, # 设置饼图的半径
        center = (0.2,0.2), # 设置饼图的原点
        textprops = {'fontsize':9, 'color':'k'}, # 设置文本标签的属性值
        pctdistance=0.6)# 设置百分比标签与圆心的距离
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
#显示图例
plt.legend(loc='lower left', bbox_to_anchor=(-0.1, 0.8))
    # loc: 表示legend的位置，包括'upper right','upper left','lower right','lower left'等
    # bbox_to_anchor: 表示legend距离图形之间的距离，当出现图形与legend重叠时，可使用bbox_to_anchor进行调整legend的位置
    # 由两个参数决定，第一个参数为legend距离左边的距离，第二个参数为距离下面的距离
plt.title('区域占比分析图')
plt.show()
