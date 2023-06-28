# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/17 18:52
"""
import threading
from time import sleep, ctime

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    """

    :param nloop:
    :param nsec:
    :return:
    """
    print("start loop ", nloop, " at:", ctime())
    sleep(nsec)
    print("loop ", nloop, " done at:", ctime())


def main():
    print("start at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # print("i:",i)
        # print("loop[i]:",loops[i])
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    print("all done at :", ctime())


if __name__ == '__main__':
    main()
