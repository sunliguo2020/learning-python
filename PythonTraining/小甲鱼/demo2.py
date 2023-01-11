# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-09 8:20
"""


def outer():
    x = 0
    y = 0

    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"现在,x={x},y = {y}")

    return inner


move = outer()
move(1, 2)
move(-2, 2)
