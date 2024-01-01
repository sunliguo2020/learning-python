# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 10:07
"""
import threading
i = 0
def sum1():
    global  i
    for x in range(1000000):
        i += x
        i -=x
    print('sum1',i)

def sum2():
    global  i
    for x in range(1000000):
        i += x
        i -=x
    print('sum2',i)

if __name__ == '__main__':
    th1 = threading.Thread(target=sum1)
    th2 = threading.Thread(target=sum2)

    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('over')