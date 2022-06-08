# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 20:05
"""

import time,os
a = 100


def f1(n):
    print("n:", id(n))
    n = n + 20
    print("n:", id(n))
    print(n)


f1(a)
print("a:", id(a))
