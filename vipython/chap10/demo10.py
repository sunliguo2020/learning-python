# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/19 13:32
"""
def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

print(fac(1))