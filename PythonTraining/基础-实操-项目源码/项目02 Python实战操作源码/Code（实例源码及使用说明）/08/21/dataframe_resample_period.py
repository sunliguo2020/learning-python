import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

aa =r'../data/TB2018.xls'
df = pd.DataFrame(pd.read_excel(aa))
df1=df[['订单付款时间','买家会员名','联系手机','买家实际支付金额']]
df1 = df1.set_index('订单付款时间') # 将date设置为index

print('---------按月统计数据-----------')
#“MS”是每个月第一天为开始日期，“M”是每个月最后一天
print(df1.resample('M').sum().to_period('M'))


print('---------按季统计数据-----------')
#“QS”是每个季度第一天为开始日期，“Q”是每个季度最后一天
print(df1.resample('QS').sum())

print('---------按年统计数据-----------')
#“AS”是每年第一天为开始日期，“A”是每年最后一天
print(df1.resample('AS').sum())

print('---------按年统计并显示数据-----------')
#“AS”是每年第一天为开始日期，“A”是每年最后一天
print(df1.resample('AS').sum().to_period('A'))
print('---------按季度统计并显示数据-----------')
print(df1.resample('Q').sum().to_period('Q'))
print('---------按月统计并显示数据-----------')
print(df1.resample('M').sum().to_period('M'))
df2=df1.resample('M').sum().to_period('M')
df2.to_excel('result2.xls')
print('---------按星期统计并显示数据-----------')
print(df1.resample('w').sum().to_period('W').head())
#print('---------近7天数据的统计-----------')
print(df1.resample('7D').sum())
#print(df1.resample('60S').last())
