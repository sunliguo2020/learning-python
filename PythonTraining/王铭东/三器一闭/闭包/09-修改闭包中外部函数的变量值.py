# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-17 7:42
"""


def counter(start=0):
    def add_one():
        nonlocal start
        start += 1
        return start

    return add_one


c1 = counter(5)
print(c1())
print(c1())
