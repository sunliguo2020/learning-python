# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-23 7:07
python 多线程实现方法
1、创建Thread的实例，传给它一个函数。
2、创建Thread的实例，传给它一个可调用的实例
3、派生Thread的子类，并创建子类的实例。

"""
import threading
import time
# 方法1 Thread类实例，target为运行的方法名称，额外的参数用args指定

from threading import Thread


def fun1(second):
    print("我是通过线程来启动的")
    print(f'Threading {threading.current_thread().name} is running.')
    time.sleep(second)
    print(f"线程启动的，{threading.current_thread().name}我要结束了")


for i in range(5):
    t = Thread(target=fun1, args=(i,))
    t.start()
    # 如果想要主线程等待子线程运行完毕之后才退出，可以让每个子线程对象都调用下 join 方法：
    t.join()

print(f'Threading {threading.current_thread().name} is ended')