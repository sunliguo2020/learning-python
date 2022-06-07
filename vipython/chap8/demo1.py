# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/12 18:39
"""
'''可变序列'''

lst = [10,20,300]
print(id(lst))
lst.append(10000)
print(id(lst))
'''不可变序列'''
s ='hello'
print(s,id(s))
s = s+'word'
print(s,id(s))