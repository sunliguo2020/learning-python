import pandas as pd
import datetime as dt
aa ='../data/5月销售数据.xls'
df = pd.DataFrame(pd.read_excel(aa))
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df1=df[['订单付款时间','买家会员名','联系手机','买家实际支付金额']]
#去除空记录
df1=df1[df1['订单付款时间'].notnull()]
df1['订单付款时间']=pd.to_datetime(df1['订单付款时间'])
#提取年、月、日
df1['年'],df1['月'],df1['日']=df1['订单付款时间'].dt.year,df1['订单付款时间'].dt.month,df1['订单付款时间'].dt.day
print(df1.head())





