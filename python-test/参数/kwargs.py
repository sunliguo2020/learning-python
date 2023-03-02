# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-23 11:32
"""


def print_score(**kwargs):
    print(kwargs, type(kwargs))
    for a, b in kwargs.items():
        print(a, b)


c = {'yuwen': 89,
     'shuxue': 95}
print(print_score(yuwen=98, shuxue=22))
print_score(**c)
