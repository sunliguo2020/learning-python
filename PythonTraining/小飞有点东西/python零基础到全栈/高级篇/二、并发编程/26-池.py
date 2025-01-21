# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-04-21 19:48
"""
import time
from concurrent.futures import ThreadPoolExecutor


def task(i):
    print("Task started", i)
    time.sleep(3)
    return i + 10


pool = ThreadPoolExecutor()
f_list = []
for i in range(50):
    future = pool.submit(task, i)  # 往线程池中提交任务
    f_list.append(future)

pool.shutdown()  # 关闭线程池，等待线程池中所有任务运行完毕

for future in f_list:
    print("任务结果:", future.result())

print("All tasks finished")
