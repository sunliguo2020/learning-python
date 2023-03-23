import pandas as pd
aa =r'../data/1月销售数据.xls'
df = pd.DataFrame(pd.read_excel(aa))

#判断每一行数据是否重复（全部相同），False表示不重复，返回值为True表示重复
print(df.duplicated())
#去除全部的重复数据
print(df.drop_duplicates())
#去除指定列的重复数据
print(df.drop_duplicates(['买家会员名']))
#保留重复行中的最后一行
print(df.drop_duplicates(['买家会员名'],keep='last'))
#inplace=True表示直接在原来的DataFrame上删除重复项，而默认值False表示生成一个副本。
print(df.drop_duplicates(['买家会员名','买家支付宝账号'],inplace=False))

