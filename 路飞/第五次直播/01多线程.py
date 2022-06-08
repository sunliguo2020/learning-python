# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/18 14:35
"""
from threading import Thread


# def func(name):
#     print(f"我是：{name}")
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=func, args=("周杰伦",))
#     t2 = Thread(target=func, args=("周润发",))
#     t1.start()
#     t2.start()

class Mythread(Thread):
    def __init__(self, name):
        super(Mythread, self).__init__()
        self.name = name

    def run(self):
        for i in range(100):
            print(self.name, i)


if __name__ == '__main__':
    t1 = Mythread('周杰伦')
    t2 = Mythread('王富贵')
    t3 = Mythread('王力宏')

    t1.start()
    t2.start()
    t3.start()
