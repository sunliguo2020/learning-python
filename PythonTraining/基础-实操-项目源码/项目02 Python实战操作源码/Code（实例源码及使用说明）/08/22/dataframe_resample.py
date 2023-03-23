import pandas as pd
aa =r'../data/datetime.xls'
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame(pd.read_excel(aa))
df = df.set_index('订单付款时间') # 将date设置为index
print(df.resample('60S').last())

#df1 = df['金额'].resample('60S', label = 'right').sum()
#df2= df['数量'].resample('60S', label = 'right').sum()
#数据合并
#df = pd.concat([df1,df2], axis = 1)
#print(df)
