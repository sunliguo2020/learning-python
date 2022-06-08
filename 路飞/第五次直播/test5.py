# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/21 18:55
"""
import time
from multiprocessing import Process

tickNum = 10


def func(num):
    """

    :param num:
    :return:
    """
    print("我是子进程，我要购买%d张票！" % num)
    global tickNum
    tickNum -= num
    time.sleep(2)


if __name__ == "__main__":
    p = Process(target=func, args=(3,))
    p.start()
    # 主进程在子进程结束之后再结束
    p.join()  # 只有当子进程结束后，join的调用结束，才会执行join后续的操作
    print("目前剩余车票数量为：", tickNum)  # 输出结果仍然是10
    # 进程和进程之间是完全独立。两个进程对应的是两块独立的内存空间，每一进程只可以访问自己内存空间的数据。
