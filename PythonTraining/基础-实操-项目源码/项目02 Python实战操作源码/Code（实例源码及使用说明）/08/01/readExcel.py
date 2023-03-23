#-*-coding:utf-8-*- 
import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
aa ='../data/TB2018.xlsx'
df = pd.DataFrame(pd.read_excel(aa))
df1= df[['买家会员名','买家实际支付金额']]
print(df1)

print('---------获取股票数据-----------')

bb ='../data/000001.csv'
df = pd.read_csv(bb,encoding = 'gbk')
df1= df[['date','open','high','close','low']]
df1.columns = ['日期','开盘价','最高价','闭市价','最低价']
print(df1)
print('---------获取文本数据-----------')
cc ='../data/fl4_name.txt'
df = pd.read_csv(cc,encoding='gbk')
print(df)
