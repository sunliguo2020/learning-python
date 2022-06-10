# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/4/9 12:39
"""
with open('./a.txt','w') as f:
    f.write('1\n2\n3\n\n')

with open('./a.txt') as f:
    print(type(f))
    for i in f:
        print(type(i))
        print(i,end='')
    my_list = f.readlines()

print(len(my_list))
print(my_list)