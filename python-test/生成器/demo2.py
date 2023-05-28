# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-28 20:14
"""
# 列表推导式
list1 = [num * num for num in range(1, 6)]

print(list1)
# 将列表推导式的方括号[] 改为小括号()即可创建一个生成器。
g = (num*num for num in range(1,6))
print(g)
print(next(g))
for i in g:
    print(i)