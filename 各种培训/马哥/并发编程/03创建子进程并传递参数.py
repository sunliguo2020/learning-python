# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 7:17
"""
from multiprocessing import Process

from time import sleep


def run_test(name, **kwargs):
    print("子进程 正在运行，name的值：%s" % name)
    print("字典kwargs", kwargs)


if __name__ == '__main__':
    print('主进程正在 进行')
    p = Process(target=run_test, args=("test",), kwargs={'key': 12})
    p.start()
