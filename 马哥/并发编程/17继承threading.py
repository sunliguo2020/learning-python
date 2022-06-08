# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/21 13:54
"""
import threading
import time


def fun1(delay):
    print(f"线程{threading.current_thread().getName()}执行fun1")
    time.sleep(delay)
    print(f"线程{threading.current_thread().name}结束")


def fun2(delay):
    print(f"线程{threading.current_thread().getName()}执行fun2")
    time.sleep(delay)
    print(f"线程{threading.current_thread().name}结束")


# 创建一个类Mythread 继承threading.Thread
class Mythread(threading.Thread):
    # 重写构造方法
    def __init__(self, func, name, args):
        super().__init__(target=func, name=name, args=args)

    def run(self):
        self._target(*self._args)


if __name__ == '__main__':
    print("开始运行")
    t1 = Mythread(fun1, "thread-1", (2,))
    t2 = Mythread(fun2, "thread-2", (4,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
