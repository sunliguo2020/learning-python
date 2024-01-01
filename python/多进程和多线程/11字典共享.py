# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 21:18
"""
from multiprocessing import Manager, Process


def test(d):
    d['name'] = 'lucky'
    d['sex'] = 'man'


if __name__ == '__main__':
    p_dict = Manager().dict()
    p = Process(target=test, args=(p_dict,))
    p.start()
    p.join()
    print(p_dict)
