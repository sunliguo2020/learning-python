# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 17:59
"""
import threading

#当前线程对象
t = threading.current_thread()
#当前线程名
print(t.name)
#当前处于活动状态的线程个数
print(threading.active_count())
#当前主线程对象
t = threading.main_thread()
print(t.name)