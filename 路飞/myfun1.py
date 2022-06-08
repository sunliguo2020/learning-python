# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/14 17:22
"""

a = [1,2,3,4]

def func(b):
    print("id(b):",id(b))
    b.append(5)
    print("函数内部b的值为：",b)

print("id(a):",id(a))
func(a)
print("函数外部a的值为：",a)