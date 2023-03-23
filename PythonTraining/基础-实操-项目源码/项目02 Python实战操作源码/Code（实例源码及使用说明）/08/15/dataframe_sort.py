import pandas as pd
excelFile = r'../data/mrbook.xlsx'
excelFile1 = r'../data/books.xls'
df = pd.DataFrame(pd.read_excel(excelFile))
dfrow = pd.DataFrame(pd.read_excel(excelFile1))
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
print('-------------------------按照一列数据排序-------------------------')
#按“销量”列降序排序
df=df.sort_values(by='销量',ascending=False)

print('-------------------------按照多列数据排序-------------------------')
#按“图书名称”和“销量”列降序排序
df.sort_values(by=['图书名称','销量'])
print(df.sort_values(by=['图书名称','销量']))

print('-------------------------对分组统计结果排序-------------------------')
df1=df.groupby(["类别"])["销量"].sum().reset_index()
df2=df1.sort_values(by='销量',ascending=False)
print(df2)

print('-------------------------按行数据排序-------------------------')
#按照索引值为0的行，即第一行的值来降序排序
dfrow.sort_values(by=0,ascending=False,axis=1)
print(dfrow)

print('-------------------------数据排名-------------------------')
#平均排名
df['平均排名']=df['销量'].rank(ascending=False)
print(df[['图书名称','销量','平均排名']])
#顺序排名
df['顺序排名']=df['销量'].rank(method="first",ascending=False)
print(df[['图书名称','销量','顺序排名']])
#最小值排名
#print(df['销量'].rank(method="min",ascending=False))
#最大值排名
#print(df['销量'].rank(method="max",ascending=False))
