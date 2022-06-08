# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 7:22
"""
from multiprocessing import Process
from time import sleep


def worker(interval):
    print("work start")
    sleep(interval)
    print("work end")


if __name__ == '__main__':
    print("主进程正在运行")
    p = Process(target=worker, args=(2,))
    p.start()

    # 希望下面的语句，在进程执行完才输出
    # sleep(5)
    # 调用join方法，主进程等待调用join的子进程结束
    p.join()
    print("主进程执行完")
