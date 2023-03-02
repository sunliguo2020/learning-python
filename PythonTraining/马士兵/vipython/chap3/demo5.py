# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/4 13:09
"""

a, b = 10, 20
print('a >b吗？', a > b)
print('a<b 吗？', a < b)

a = 10
b = 10
print('id a', id(a))
print('id b', id(b))
print(a == b)  # value 相等
print(a is b)  # a与b的id标识 相等

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

print(a == b)
print(a is b)
