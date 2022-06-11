# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 7:29
"""
import multiprocessing
import time


def clock(interval):
    for i in range(3):
        print("当前时间：", time.ctime())
        time.sleep(interval)


if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(1,))
    p.start()
    p.join()
    print('p.pid', p.pid)
    print("p.name", p.name)
    print("p.is_alive", p.is_alive())
