# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 9:33
"""
import threading
import time


def run(i):
    print('子线程开始', threading.current_thread().name)
    print(f"{i}开始干活")
    time.sleep(3)
    print(f"{i}干活结束")


if __name__ == '__main__':
    t1 = time.time()
    t_list = []
    for i in range(5):
        thr = threading.Thread(target=run, args=(i,))
        thr.start()
        t_list.append(thr)
    # for it in t_list:
    #     it.start()
    #     it.join()
    for j in t_list:
        j.join()
    print('over')
    print(time.time() - t1)
