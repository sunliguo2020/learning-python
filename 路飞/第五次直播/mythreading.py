# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/18 8:43
"""
import time
from threading import Thread


def func(num):
    time.sleep(2)
    print("num的值为：", num)


if __name__ == '__main__':
    # 创建好一个子线程
    t = Thread(target=func, args=(1,))
    t.start()
