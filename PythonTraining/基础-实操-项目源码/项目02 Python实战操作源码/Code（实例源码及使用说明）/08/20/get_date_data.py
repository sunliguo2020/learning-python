import pandas as pd
aa =r'../data/mingribooks.xls'
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame(pd.read_excel(aa))
df1=df[['订单付款时间','买家会员名','联系手机','买家实际支付金额']]
df1=df1.sort_values(by=['订单付款时间'])
df1 = df1.set_index('订单付款时间') # 将date设置为index

#获取某个区间数据
print(df1['2018-05-11':'2018-06-10'])


#dataframe的truncate函数可以获取某个时期之前或之后的数据，或者某个时间区间的数据
print('---------获取某个时期之前或之后的数据-----------')
print('--------after------------')
#print(df1.truncate(after='2018-01'))
print('--------before------------')
#print(df1.truncate(before='2018-1'))
