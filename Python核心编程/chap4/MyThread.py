# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/17 18:52
"""
import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.res = None

    def getResult(self):
        return self.res

    def run(self):
        print("starting", self.name, "at", ctime())
        self.res = self.func(*self.args)
        print(self.name, "finished at:", ctime())


if __name__ == '__main__':
    pass
