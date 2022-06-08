# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/29 13:01
"""

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("Error:Invalid argument.")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))