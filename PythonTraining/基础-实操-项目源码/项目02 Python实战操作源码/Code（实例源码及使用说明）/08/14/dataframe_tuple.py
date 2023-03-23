import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
aa =r'../data/fl4.xls'
df = pd.DataFrame(pd.read_excel(aa))
df2=df[['label1','label2']]
print(df2)
tuples = [tuple(x) for x in df2.values]
print(tuples)
