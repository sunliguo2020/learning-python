# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-09 13:22
"""


def myfunc(*args, a, b):
    print(f"有{len(args)}个参数")
    print(args, a, b)


myfunc(1, 2, 3, 4)
