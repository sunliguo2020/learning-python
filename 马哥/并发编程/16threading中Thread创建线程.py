# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/21 13:25
"""
import threading
import  time
def fun1(thread_name,delay):
    print(f"线程1{thread_name}开始运行")
    time.sleep(delay)
    print(f"线程1{thread_name}结束运行")


def fun2(thread_name, delay):
    print(f"线程2{thread_name}开始运行")
    time.sleep(delay)
    print(f"线程2{thread_name}结束运行")

if __name__ == '__main__':
    t1 = threading.Thread(target=fun1,args=("thread1",2))
    t2 = threading.Thread(target=fun2,args=("thread1",3))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("主进程结束")17