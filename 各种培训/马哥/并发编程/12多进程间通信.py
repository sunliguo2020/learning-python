# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 21:08
"""
import time
from multiprocessing import Process,Queue

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
    q =  Queue()
    pw =Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()
    pr.join()
    pw.join()

