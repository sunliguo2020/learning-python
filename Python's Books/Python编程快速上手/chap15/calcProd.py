# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/19 21:10
"""
import time


def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print("The result is %s digits long." % len(str(prod)))
print("Took %s second to calculate." % (endTime - startTime))
