# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-28 12:54
"""
__all__ = ['name']
print('我是module')
name = '张大仙'


def func1():
    print('我是func1')


def func2():
    print('我是func2')
    global name
    name = '周杰伦'


def get():
    print(name, id(name))
