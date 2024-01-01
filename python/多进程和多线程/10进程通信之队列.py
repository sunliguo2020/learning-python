# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 21:08
"""
from multiprocessing import Process, Queue


def test(q):
    q.put('a')
    q.put('b')
    q.put('c')


if __name__ == '__main__':
    q = Queue()
    p = Process(target=test, args=(q,))
    p.start()
    p.join()
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get(timeout=3))
