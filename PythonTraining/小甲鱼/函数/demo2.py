# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-09 13:20
"""


def abc(a, *, b, c):
    print(a, b, c)


print(abc(1, b=2, c=3))
