# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/6/13 18:38
"""


def eggs(someParameter):
    print(id(someParameter))
    someParameter.append('Hello')


spam = [1, 2, 3]
print(id(spam))
eggs(spam)
print(spam)
