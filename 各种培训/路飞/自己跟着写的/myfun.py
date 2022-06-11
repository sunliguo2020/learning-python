# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/14 17:40
"""
a = 1
def  func(b):
    b = 2
    print("id(b)",id(b))
    print("b的值为：",b)


func(a)
print("a的值为",a)
print("id(a)",id(a))