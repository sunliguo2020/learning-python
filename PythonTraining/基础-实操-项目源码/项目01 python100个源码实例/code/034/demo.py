import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
#获取数据
df=pd.read_excel('accounts.xlsx')
#设置索引，按月份显示数据
df=df.set_index('日期',drop=True)
df=df['2019'].to_period('M') # 获取2019年每个月的数据
#按月统计支出
df_month=df.groupby(['日期'])[['金额']].sum().reset_index()
#环比差值
df_month['差值']=df_month.金额-df_month.金额.shift()
print(df_month)

