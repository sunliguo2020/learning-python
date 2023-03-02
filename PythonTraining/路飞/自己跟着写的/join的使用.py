# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 20:06
"""
import time
from multiprocessing import Process


def func(args):
    print("我是子进程")
    time.sleep(args)
    print("子进程结束")


if __name__ == '__main__':
    print("主进程开始")
    p = Process(target=func, args=(4,))
    p.start()
    p.join()
    print("主进程结束")
