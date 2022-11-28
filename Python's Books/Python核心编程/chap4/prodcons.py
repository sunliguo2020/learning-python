# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/22 15:13
"""
from queue import Queue
from random import randint
from time import sleep

from MyThread import MyThread


def writeQ(queue):
    print("producing object for Q...")
    Queue.put('xxx', 1)


def readQ(queue):
    val = Queue.get(1)
    print("consumed object from Q... size now,", queue.qsize())


def write(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [write, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()

    print("all done")


if __name__ == '__main__':
    main()
