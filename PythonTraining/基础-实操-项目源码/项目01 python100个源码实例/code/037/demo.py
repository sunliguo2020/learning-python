import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
#获取数据
df=pd.read_excel('accounts.xlsx')
#设置索引，按年份显示数据
df=df.set_index('日期',drop=True)
df=df.to_period('A')
#按支出类别分组统计
df_year=df.groupby(['日期','支出类别'])[['金额']].sum()
print(df_year)
