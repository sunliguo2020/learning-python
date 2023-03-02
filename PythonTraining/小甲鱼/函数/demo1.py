# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-09 13:07
"""


def myfunc(name):
    for i in range(3):
        print(f"I love {name}")


myfunc('python')


def myfunc1(s, vt, o):
    return "".join((o, vt, s))


print(myfunc1('我', '打了', '小甲鱼'))
