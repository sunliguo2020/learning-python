# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 7:40
"""
import time
from multiprocessing import Process


class ClockProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print("子进程开始的时间，{}".format(time.ctime()))
        time.sleep(self.interval)
        print("子进程结束时间；{}".format(time.ctime()))


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    p.join()
    print("主进程执行完")
