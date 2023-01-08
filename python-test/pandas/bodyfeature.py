# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-02 16:23
通过pandas删除列：

1.del df['columns'] #改变原始数据

2.df.drop('columns',axis=1)#删除不改表原始数据，可以通过重新赋值的方式赋值该数据

3.df.drop('columns',axis=1,inplace=True) #改变原始数据

"""
import pandas as pd

bodyfeature_file = r'Y:\sgy\jiankang\data_handing\bodyfeature_csv-20220208\a.txt'
dataFrame = pd.read_csv(bodyfeature_file, header=0,low_memory=False)
print(type(dataFrame))

dataFrame.drop('errno',axis=1,inplace=True)
dataFrame.drop('errmsg',axis=1,inplace=True)
dataFrame.drop('content',axis=1,inplace=True)

dataFrame.to_csv('bodyfeature-20230103.csv')