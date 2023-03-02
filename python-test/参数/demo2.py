# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-05 13:10
可变参数
"""


def abc(a, **b):
    print(a)
    print(b)


abc(100,b=200,k=30)
