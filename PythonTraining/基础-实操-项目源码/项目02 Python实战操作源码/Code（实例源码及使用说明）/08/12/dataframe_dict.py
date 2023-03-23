import pandas as pd
aa ='../data/mingribooks.xls'
df = pd.DataFrame(pd.read_excel(aa))
df1=df.groupby(["宝贝标题"])["宝贝总数量"].sum()

df1.to_excel('dict.xls')

mydict=df1.to_dict()
print(mydict)
#遍历字典
#for item in mydict.items():
#  print(item)
