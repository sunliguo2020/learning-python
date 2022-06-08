# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/21 18:35
"""
import os
import time
from multiprocessing import Process


def func(num1, num2):
    """

    :param num1:
    :param num2:
    :return:
    """
    print("我是子进程")
    time.sleep(1)
    print("子进程ID号：", os.getpid())
    print("该子进程的父进程ID号：", os.getppid())
    print('我是绑定给子进程的一组任务！', num1, num2)


if __name__ == "__main__":
    print('主进程开始执行！主进程的ID', os.getpid())

    # 创建一个进程p，给该进程绑定一组任务
    p = Process(target=func, args=(123, 456))
    p.start()
    print("主进程执行结束！")
