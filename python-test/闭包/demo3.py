# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-06 18:30
计数器
"""


def func1():
    counter = [0]

    def inner():
        counter[0] += 1
        print(f"当前是第{counter[0]}次访问")

    return inner


counter = func1()
counter()
counter()
counter()
