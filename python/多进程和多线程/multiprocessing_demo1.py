# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/5 15:07
"""
import multiprocessing
import os
import time
import random

def f():
    """

    :return:
    """
    time.sleep(random.randint(0, 10))
    print(os.getpid())


class MyProcess(multiprocessing.Process):
    """

    """
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):

        f()


if __name__ == '__main__':
    print(os.getpid())
    p = multiprocessing.Process(target=f)
    p.start()
    p.join()

    p = MyProcess()
    p.start()
    p.join()
