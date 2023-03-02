# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-06 17:09
闭包：
1、外部函数中定义内部函数
2、外部函数有返回值
3、返回值的的内部函数名
4、内部函数引用外部函数变量值
格式：

def 外部函数():
    def 内部函数():
        ...
    return 内部函数

"""


def fun1():
    a = 100

    def inner():
        b = 200
        print(a, b)

    print(locals())

    return inner


x =fun1()
x()
