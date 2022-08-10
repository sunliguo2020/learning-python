# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/10/26 13:28
"""
'''

'''
nested = [[1, 2], [3, 4], [5]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


for i in flatten(nested):
    print(i)
