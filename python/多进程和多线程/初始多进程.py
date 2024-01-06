# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 19:54
"""
import time
from multiprocessing import Process


def fun():
    print("我是fun函数")
    time.sleep(1000)


if __name__ == '__main__':
    p = Process(target=fun, name='我的进程')
    print(p)
    p.start()
    print('luncy is a good man')
