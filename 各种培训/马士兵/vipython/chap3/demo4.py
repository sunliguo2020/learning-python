# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/3 12:48
"""
i = 3 + 4
print(i)

a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))
print('-'*10)
a = 20
a+= 30
print(a)

a,b,c = 10,20,30
print(a,b,c)