# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 20:29
"""
import time
from multiprocessing import Pool


def fun1(name):
    print(f'我是{name},fun1开始')
    time.sleep(10)
    print(f"我是{name},fun1结束")


def fun2():
    print('fun2开始')
    time.sleep(5)
    print("fun2结束")


if __name__ == '__main__':
    pp = Pool()
    for i in range(1, 11):
        pp.apply_async(fun1, args=(i,))
    pp.close()
    pp.join()
    print('over')
