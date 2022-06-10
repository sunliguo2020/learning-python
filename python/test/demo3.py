# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/14 11:36
"""


def fun1(ar):
    print("id(ar)", id(ar))
    print("ar", ar)
    ar = 2


ar = 1
print(id(ar))
fun1(ar)
print(ar)
