# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-06 17:34
"""
def func(a,b):
    c = 100
    def inner():
        print('a+b+c',a+b+c)

    return inner

fun1 = func(10,20)
fun2 = func(30,40)
fun2()
fun1()
