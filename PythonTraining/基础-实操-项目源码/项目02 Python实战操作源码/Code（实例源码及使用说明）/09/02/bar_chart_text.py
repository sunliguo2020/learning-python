import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aa =r'../data/mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(aa))
df1=df[['序号','图书名称','销量']]
df1=df1.sort_values('销量',ascending=False)
#创建一个长10英寸，宽6英寸的窗口
plt.figure(figsize=(10,6))
y=np.array(list(df1['销量'])) #设置y轴的数值
xticks1=list(df1['图书名称']) #构造不同数列
x=range(len(xticks1))
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
#画出柱形图
plt.bar(x,y,width = 0.5,align='center',color = 'c',alpha=0.8)
#设置x轴的刻度，将构建的xticks代入，设置字体和对齐方式
plt.xticks(range(len(xticks1)),xticks1,fontsize=6,rotation=90)
#x、y轴标签
plt.xlabel('图书名称')
plt.ylabel('销量')
plt.title('月销量分析')
#设置标签**
for a,b in zip(x,y):
  plt.text(a, b+10, '%.0f' % b, ha='center', va= 'bottom',fontsize=9)
#设置y轴的范围
plt.ylim(0,2500)
plt.show()
