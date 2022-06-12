# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/17 18:51
"""


def fun(a, b=10):
    print("a=", a)
    print("b=", b)


def fun2(*args):
    print(args)


def fun3(**args):
    print(args)


fun2(10, 20, 30, 40)


def fun4(a, b, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


fun4(10, 203, 30, 40)

fun4(10, 30, c=30, d=40)
