# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/19 13:24
"""


def fun(a, b):  # a b 形参
    c = a + b  # c为局部变量
    print(c)


"""print(c)
print(a, b)
"""
name = '杨老师'  # name 的作用范围为函数内部和外部都可以使用 全局变量
print(name)


def fun2():
    print(name)


fun2()


def fun3():
    global age
    age = 20
    print(age)


fun3()
print(age)
