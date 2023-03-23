# -*- coding:utf-8-*-
import pandas as pd
aa ='../data/mingribooks.xls'
df = pd.DataFrame(pd.read_excel(aa))
df1=df[['宝贝标题']]
#list1=df1.values.tolist()
#去除重复记录，使用tolist转成list
list1=df1['宝贝标题'].drop_duplicates().values.tolist()

print(list1)

