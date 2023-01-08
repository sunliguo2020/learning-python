# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-05 13:06
"""


def abc(a, *args):
    print(a)
    print(args)


abc(10, )
abc(10, 20, 30, 40)
