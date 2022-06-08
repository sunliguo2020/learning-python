# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/14 17:48
"""
def func(a=[]):
    print('id(a)',id(a))
    a.append('A')
    return a

print(func())
print(func())
print(func())