import pandas as pd
aa =r'../data/TB2018a.xls'
df = pd.DataFrame(pd.read_excel(aa))
#设置数据显示的行、列和宽等,解决输出结果显示不全的问题
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

#删除空值，订单付款时间非空值才保留
#删除买家实际支付金额为0的记录
df1=df[df['订单付款时间'].notnull() & df['买家实际支付金额'] !=0]

#空值用0填充
df['宝贝总数量'] = df['宝贝总数量'].fillna(0)
print(df)
#print(df[['买家会员名','买家实际支付金额','宝贝总数量']])
#保存
df1.to_excel('../data/result.xls')
