# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/17 18:52
"""
import _thread
from time import sleep,ctime

loops=[4,2]

def loop(nloop,nsec,lock):
    print("start ",nloop,"at", ctime())
    sleep(nsec)
    print("loop",nloop," done at:", ctime())
    lock.release()

def main():
    print("start at:", ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    print("all Done at:",ctime())


if __name__ == '__main__':
    main()
