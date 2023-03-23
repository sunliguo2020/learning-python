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
df_month_sort['占比']=(df_month_sort['金额']/df['金额'].sum()).apply(lambda x: format(x, '.2%'))
#添加行索引
df_month_sort.index=[1,2,3,4,5,6]
print('2019年12月总支出：',df_month['金额'].sum(),'元')
print(df_month_sort)


