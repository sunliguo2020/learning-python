# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/22 18:56
"""
import pickle
import json
def a():
    pass
dict1 = {
    "key1":'value1'
}
x = pickle.dumps(dict1)
print(x,type(x))

data = pickle.loads(x)
print(data,type(data))
with open('aa.txt',"wb") as fp:
    pickle.dump(dict1,fp)

with open("aa.txt",'rb') as fp:
    print(fp.read())
print(pickle.load(open("aa.txt",'rb')))

json.dump({'k1':"python姓名"},open("b.txt",'w'))