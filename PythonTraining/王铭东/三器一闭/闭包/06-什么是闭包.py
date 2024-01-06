# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 18:48
什么是闭包？
如果一个函数中又嵌套定义了另外一个函数，且 内部的这个函数用到了外部函数的局部变量或者形参，
那么这个内部函数以及用到的外部函数中的变量 称之为闭包。
怎么定义闭包？
1、函数嵌套定义
2、内部函数用到外部函数的变量
3、外部函数将内部函数的引用返回。

"""


def person(name):
    num = 100

    def say(content):
        print(f"{name}:{content}")

    return say
