# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 20:44
"""
from multiprocessing import Process

name = 'lucky'


def test1():
    global name
    print(name)
    name = 'lisi'
    print(name)


if __name__ == '__main__':
    p = Process(target=test1, )
    p.start()
    p.join()
    print(name)
