# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 10:29
"""
import time
from concurrent.futures import ThreadPoolExecutor


def run(i):
    print(f'线程{i}开始')
    time.sleep(2)
    print(f"线程{i}结束")


if __name__ == '__main__':
    List = [1, 2, 3, 4, 5]
    pool = ThreadPoolExecutor(3)
    # 方式1
    # for i in List:
    #     pool.submit(run,i)

    # 简写
    # task_list = [pool.submit(run,i) for i in List]
    # wait(task_list)

    pool.map(run, List)

    print('over')
