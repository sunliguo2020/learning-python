import pandas as pd
aa ='../data/TB2018.xlsx'

df = pd.DataFrame(pd.read_excel(aa))
series=df['收货地址'].str.split(' ',expand=True)
df['省']=series[0]
#df['省'],df['市'],df['区']=series[0],series[1],series[2]
df1=df.groupby(["省"])["买家实际支付金额"].sum()
print(df1)

df.to_excel('test.xlsx')

