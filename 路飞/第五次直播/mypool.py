# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/18 8:48
"""
from multiprocessing.dummy import Pool
import time

urls =["www.1.com",
       "www.2.com",
       "www.3.com"]

def get_request(url,t):
    print("正在请求的数据：",url)
    time.sleep(t)
    print("请求结束：",url)

start  = time.time()
#创建一个线程池，开启了5个线程
pool = Pool(5)
#可以利用线程池中的3个线程不断地去处理5个任务
pool.map(get_request,urls,[1,2,3])
#get_request函数调用次数取决于urls列表元素的个数
#get_request 每次执行都会接受urls列表中的一个元素作为参数

print("总耗时；",time.time()-start)
pool.close()