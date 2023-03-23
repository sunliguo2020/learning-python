import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set_style('darkgrid')
file ='./data/mrtb_data.xlsx'
df = pd.DataFrame(pd.read_excel(file))
plt.rc('font', family='SimHei', size=13)
# 通过reset_index()函数将groupby()的分组结果重新设置索引
df1 = df.groupby(['类别'])['买家实际支付金额'].sum()
df2 = df.groupby(['类别','性别'])['买家会员名'].count().reset_index()
men_df=df2[df2['性别']=='男']
women_df=df2[df2['性别']=='女']
men_list=list(men_df['买家会员名'])
women_list=list(women_df['买家会员名'])
num=np.array(list(df1))  #消费金额
#计算男性用户比例
ratio=np.array(men_list)/(np.array(men_list)+np.array(women_list))
np.set_printoptions(precision=2) #使用set_printoptions设置输出的精度
#设置男生女生消费金额
men = num * ratio
women = num * (1-ratio)
df3=df2.drop_duplicates(['类别'])   #去除类别重复的记录
name=(list(df3['类别']))
#生成图表
x = name
width = 0.5
idx = np.arange(len(x))
plt.bar(idx, men, width,color='slateblue', label='男性用户')
plt.bar(idx, women, width, bottom=men, color='orange', label='女性用户')
plt.xlabel('消费类别')
plt.ylabel('男女分布')
plt.xticks(idx+width/2, x, rotation=20)
#在图表上显示数字
for a,b in zip(idx,men):
    plt.text(a, b, '%.0f' % b, ha='center', va='top',fontsize=12)  #对齐方式'top', 'bottom', 'center', 'baseline', 'center_baseline'
for a,b,c in zip(idx,women,men):
    plt.text(a, b+c+0.5, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)
plt.legend()
plt.show()
