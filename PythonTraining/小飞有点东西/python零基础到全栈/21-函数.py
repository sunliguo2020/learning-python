# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-28 8:42
"""
import time

#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         name = input('请输入密码：')
#         if name == 'sunliguo':
#             res = func(*args, **kwargs)
#             return res
#         else:
#             print('用户名错误！')
#
#     return wrapper
#
#
# @outer
# def home():
#     time.sleep(2)
#     print('home')
#
#
# home()

#
# def func1():
#     print(x)
#
#
# x = 10
# func1()

x = 10


def func1():
    print(x)


def func2():
    x = 20
    func1()
    x += 1


func2()
