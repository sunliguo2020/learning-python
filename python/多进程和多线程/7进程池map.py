# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 20:38
"""
import time
from multiprocessing import Pool


def fun1(name):
    print(f'我是{name},fun1开始')
    time.sleep(10)
    print(f"我是{name},fun1结束")


if __name__ == '__main__':
    p = Pool()
    t_list = list(range(1, 11))
    p.map(fun1, t_list)
