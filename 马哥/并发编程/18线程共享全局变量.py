# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/21 14:08
"""
from threading import Thread
num = 10


def test1():

    global num
    for i in range(2):
        num += 1
    print("执行test后,num:",num)
    print("test1 id(num):",id(num))
def test2():
    print("test2 num的值：",num)
    print("test2 id(num):", id(num))

if __name__ == '__main__':
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t1.join()
    t2.start()
    t2.join()

