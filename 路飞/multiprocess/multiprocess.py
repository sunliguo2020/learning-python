# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/14 18:44
"""
import multiprocessing.process
from multiprocessing import Process
import time


def fun1(name, i):
    print(f"我是进程 {i}",multiprocessing.process.current_process().name)
    #print(name, i)
    time.sleep(2)
    print(f"进程{i}结束")


if __name__ == '__main__':
    start_time = time.time()
    process_list = []  # 创建存储好的子进程
    for i in range(10):
        p = Process(target=fun1, args=('pyton', i,))
        process_list.append(p)
        p.start()

    for pp in process_list:
        pp.join()

    print("测试完成-", time.time() - start_time)