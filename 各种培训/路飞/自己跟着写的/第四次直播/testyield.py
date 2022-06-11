# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/18 22:13
"""


def yieldTest():
    """

    :return:
    """
    i = 0
    while i < 3:
        temp = yield i
        print(temp)
        i = i + 3
