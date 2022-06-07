# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/13 17:42
"""
s1 = {10, 20, 30, 40}
s2 = {40, 30, 20, 10}
#两个集合是否相等
print(s1 == s2)
print(id(s1), id(s2))
#一个集合是否是另一个集合的子集
s1 = {10,20}
s2 = {10,20,30}
print(s2.issubset(s1))
print(s1.issubset(s2))