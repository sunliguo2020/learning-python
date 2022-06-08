# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 7:14
"""
from multiprocessing import Process


def run_test():
    print("test")


if __name__ == '__main__':
    print("主进程正在进行---")
    p = Process(target=run_test)
    p.start()
