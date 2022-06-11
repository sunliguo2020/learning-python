# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/17 12:44
"""
import threading
import time


def run():
    time.sleep(2)
    print("当前线程的名字是：", threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':
    start_time = time.time()
    print("这是主线程：", threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()

    print("主线程结束", threading.current_thread().name)
    print("一共用时：", time.time() - start_time)
