import pandas as pd
#import numpy as np
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
excelFile = r'../data/5月销售数据.xls'
df = pd.DataFrame(pd.read_excel(excelFile))
df = df.set_index('订单付款时间') # 将date设置为index
df1=df.resample('w').sum().to_period('w')
print(df1)

print('----------------宽表变长表-------------------------\n')
data1=df1.stack()
print(data1)
