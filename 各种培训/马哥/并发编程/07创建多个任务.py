# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 7:34
"""
from time import sleep
from multiprocessing import Process

def work1(interval):
    print("work1 start")
    sleep(interval)
    print("end work1")

def work2(interval):
    print("work2 start")
    sleep(interval)
    print("end work2")

def work3(interval):
    print("work3 start")
    sleep(interval)
    print("end work3")

if __name__ == '__main__':
    print("主进程开始运行")
    p1 = Process(target=work1,args=(4,))
    p2 = Process(target=work2, args=(3,))
    p3 = Process(target=work3, args=(2,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("p1.name",p1.name)