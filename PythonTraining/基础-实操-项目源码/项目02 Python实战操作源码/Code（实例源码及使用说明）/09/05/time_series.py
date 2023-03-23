import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
aa ='../data/TB2.xls'
df = pd.DataFrame(pd.read_excel(aa))
df1=df[['订单付款时间','买家会员名','联系手机','买家实际支付金额']]
df1 = df1.set_index('订单付款时间') # 将date设置为index


print('---------按季统计数据-----------')
#“QS”是每个季度第一天为开始日期，“Q”是每个季度最后一天
df2=df1.resample('QS').sum().to_period('Q')
print('---------按年统计数据-----------')
df3=df1.resample('AS').sum().to_period('A')
df2.plot()
df3.plot()
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.show()
