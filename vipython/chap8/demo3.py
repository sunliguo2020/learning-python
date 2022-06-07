# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/12 19:02
"""

t = (10,[20,30],9)
print(t,type(t))

print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

'''尝试t[1]修改为100'''
print(id(100))
#t[1] = 100 #元组不允许修改元素
#由于[20,30]列表，列表是可变序列，
t[1].append(40)
print(t,id(t[1]))