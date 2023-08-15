# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 18:35
"""
# 复习一
a = [11, 22, 33]
b = a
a.append('4')
print(a)
print(b)


# 复习二
def xx(temp):
    print(temp)
    temp.append('4')
    print(temp)


nums = [100, 200]
xx(nums)
print(nums)
