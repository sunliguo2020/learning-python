# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-28 20:21
"""


def square(input):
    list1 = []
    for num in range(input):
        print('before yield')
        yield num * num
        print('after yield')


for num in square(5):
    print(num)
