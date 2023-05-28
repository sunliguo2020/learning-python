# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-28 20:19
"""


def square(input):
    list1 = []
    for num in range(input):
        list1.append(num * num)
        print(list1)

    return list1


for num in square(5):
    print(num)
