# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 20:47
"""
from multiprocessing import Process

num = 10


def work1():
    global num
    num += 5
    print("子进程work1运行后num的 值,", num)


def work2():
    global num
    num += 10
    print("子进程work2运行后num的 值,", num)


if __name__ == '__main__':
    print("主进程开始运行")
    p1 = Process(target=work1)
    p2 = Process(target=work2)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("全局变量nu",num)