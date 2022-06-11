# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 20:36
"""
import multiprocessing
import time


def func(msg):
    print("start:", msg)
    time.sleep(3)
    print("end :", msg)


if __name__ == '__main__':
    # 创建初始化3个的进程池
    pool = multiprocessing.Pool(3)
    # 添加任务
    for i in range(1, 6):
        msg = "任务%d" % i
        pool.apply_async(func, (msg,))
    # 如果进程池不再接受新的请求
    pool.close()
    pool.join()
