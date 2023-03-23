import matplotlib.pyplot as plt
import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
#获取数据
df=pd.read_excel('accounts.xlsx')
#设置索引，按月份显示数据
df=df.set_index('日期',drop=True)
df=df['2019-12'].to_period('M') # 获取2019年12月数据
#按支出类别分组统计
df_month=df.groupby(['支出类别','日期'])[['金额']].sum().reset_index()
#按金额排序
df_month_sort=df_month[['支出类别','金额']].sort_values(by='金额',ascending=False)
#添加行索引
df_month_sort.index=[1,2,3,4,5,6]
print('2019年12月总支出：',df_month['金额'].sum(),'元')
print('我最爱把钱花在')
print(df_month_sort.rename(columns={'支出类别':'','金额':''})) #设置列名空，输出
'''
环形图表
'''
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
labels = df_month_sort['支出类别'].values.tolist()
data_percent = df_month_sort['金额'].values.tolist()
colors = ['c', 'r', 'y', 'g', 'gray','b']
wedges1, texts1, autotexts1 = plt.pie(data_percent,
    autopct = '%3.1f%%',
    radius = 1,
    pctdistance = 0.85,
    colors = colors,
    startangle = 180,
    textprops = {'color': 'w'},
    wedgeprops = {'width': 0.4, 'edgecolor': 'w'}
)
# 图例
plt.legend(wedges1,
          labels,
          fontsize = 12,
          loc = 'center right',
          borderaxespad=0., #borderaxespad将图例放外面
          frameon=False,     #去掉图例边框
          bbox_to_anchor = (1.3, 0.6))
# 设置文本样式
plt.setp(autotexts1, size=12, weight='bold')
plt.setp(texts1, size=10)
# 标题
plt.title('我最爱把钱花在', fontsize=20)
plt.show()



