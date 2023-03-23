import pandas as pd
import numpy
from pyecharts import Bar,Line,Overlap

aa =r'../data/TB2018.xls'
df = pd.DataFrame(pd.read_excel(aa))
df1=df[['订单付款时间','买家实际支付金额']]
df1 = df1.set_index('订单付款时间') # 将date设置为index
df2=df1.resample('M').sum().to_period('M')
#取整数
y=df2['买家实际支付金额'].apply(numpy.round)
print(df2)
x=["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
bar=Bar('月销量分析',background_color='darkcyan')
#bar.add('',x,y)
#设置颜色
bar.use_theme('dark')
#为图形添加最小值、最大值和均值
bar.add('',x,y,is_label_show=True,mark_point=['min','max'],mark_line=['average'])
bar.render('sales1.html')

