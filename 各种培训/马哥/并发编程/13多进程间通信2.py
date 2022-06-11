# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 21:08
"""
import time
from multiprocessing import Process,Queue,Pool,Manager

from time import  sleep

def write(q):
    a = ['a','b','c','d']
    for i in a:
        print("开始写入的值，",i)
        q.put(i)
        sleep(1)
def read(q):
    #for i  in range(q.qsize()):
    while not q.empty():
        print("正在读取的值：",q.get())
        time.sleep(1)

if __name__ == '__main__':
    q =Manager().Queue()

    pool = Pool(3)
    pool.apply(write,(q,))
    pool.apply(read,(q,))

    pool.close()
    pool.join()

