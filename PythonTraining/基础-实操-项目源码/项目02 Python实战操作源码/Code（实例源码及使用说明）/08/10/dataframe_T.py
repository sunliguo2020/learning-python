import pandas as pd
aa ='../data/TB2018.xlsx'
resultfile=r'data.xls'
df = pd.DataFrame(pd.read_excel(aa))
df1=df[['订单付款时间','买家会员名','买家实际支付金额']]
df1 = df1.set_index('订单付款时间')  #将“订单付款日期”设置为索引
# 按季度统计并显示
Q_df=df1.resample('Q').sum().to_period('Q').T
print(Q_df)#输出结果
Q_df.to_excel(resultfile) #导出结果



