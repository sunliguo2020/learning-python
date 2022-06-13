# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/11 7:30
"""
lst = [20, 40, 10, 98, 54]

print('排序前的列表', lst, id(lst))

lst.sort(reverse=True)
print('排序后的列表', lst, id(lst))

print(sorted(lst))