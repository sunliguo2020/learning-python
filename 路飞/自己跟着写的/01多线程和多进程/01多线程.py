# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 10:09
"""
import time
from threading import Thread


# def func(name):
#     for i in range(10):
#         print(name,i)
#
# if __name__ == '__main__':
#     func('周杰伦')
#     func('王力宏')
#     func("周润发")
# 创建任务
def func(name, tim=2):
    for i in range(tim):
        time.sleep(2)
        print(name, i)


if __name__ == '__main__':
    # 创建线程
    t_list = []
    t1 = Thread(target=func, args=('周仁丰', 2))
    t2 = Thread(target=func, args=('王力宏', 4))
    t1.start()
    t_list.append((t1))
    t2.start()
    t_list.append(t2)

    for i in t_list:
        i.join()
    print("主线程运行")
