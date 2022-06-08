# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/25 9:48
"""
import multiprocessing


def f(x):
    return x * x


if __name__ == '__main__':
    with multiprocessing.Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
