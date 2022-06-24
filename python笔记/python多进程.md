### python 多进程

Process（[group ]

方法：

start（）

join（[timeout]）等待进程p终止，Timeout是可选的

```python
from multiprocessing   import Process
from time import sleep

def worker(interval):
    print("work start")
    sleep(interval)
    print("work end")

if __name__ == '__main__':

    print("主进程正在运行")
    p = Process(target=worker,args=(2,))
    p.start( )

    #希望下面的语句，在进程执行完才输出
    #sleep(5)
    #调用join方法，主进程等待调用join的子进程结束
    p.join()
    print("主进程执行完")
```





Process 实例属性值

***name*** 进程的名称

- ##pid## 进程的id

```python
from multiprocessing import Process
def func():
    print("我是绑定给子进程的一组任务")
 
if __name__ == "__main__":
    print("主进程开始")
    p =Process(target = func)
    p.start()
    print("主进程执行结束")

```

创建多个任务

```python
from time import sleep
from multiprocessing import Process

def work1(interval):
    print("work1 start")
    sleep(interval)
    print("end work1")

def work2(interval):
    print("work2 start")
    sleep(interval)
    print("end work2")

def work3(interval):
    print("work3 start")
    sleep(interval)
    print("end work3")

if __name__ == '__main__':
    print("主进程开始运行")
    p1 = Process(target=work1,args=(4,))
    p2 = Process(target=work2, args=(3,))
    p3 = Process(target=work3, args=(2,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("p1.name",p1.name)
```



传递参数

```python
from multiprocessing import Process

from  time import sleep

def run_test(name,**kwargs):
    print("子进程 正在运行，name的值：%s"% name)
    print("字典kwargs",kwargs)

if __name__ == '__main__':
    print('主进程正在 进行')
    p = Process(target=run_test,args=("test",),kwargs={'key':12})
    p.start()
```

使用类创建进程

```python
import time
from multiprocessing import Process


class ClockProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print("子进程开始的时间，{}".format(time.ctime()))
        time.sleep(self.interval)
        print("子进程结束时间；{}".format(time.ctime()))


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    p.join()
    print("主进程执行完")

```





异步效果：

```py
import time
from multiprocessing import Process
def get_request(url):
    print('正在请求网址的数据：',url)
    time.sleep(2)
    print('请求结束:',url)

if __name__ == "__main__":
    urls = ['www.1.com','www.2.com','www.3.com']
    for url in urls:
        #创建了三个进程，表示三组任务
        p = Process(target=get_request,args=(url,))
        p.start()
```

进程池

Pool([numprocess[,initializer[,initargs]]])

numprocess :要创建的进程数

Pool类的实例方法：

apply（）  在一个进程池中执行函数(*args,**kargs),然后返回结果

apply_async(func,args,kwargsk,callback) 在一个进程池 中异步地执行函数(*args,**kwargs),然后返回结果。

```python
import multiprocessing
import time


def func(msg):
    print("start:", msg)
    time.sleep(3)
    print("end :", msg)


if __name__ == '__main__':
    # 创建初始化3个的进程池
    pool = multiprocessing.Pool(3)
    # 添加任务
    for i in range(1, 6):
        msg = "任务%d" % i
        pool.apply_async(func, (msg,))
    # 如果进程池不再接受新的请求
    pool.close()
    pool.join()

```

进程池中进程间通信

```python
# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 21:08
"""
import time
from multiprocessing import Process,Queue,Pool,Manager

from time import  sleep

def write(q):
    a = ['a','b','c','d']
    for i in a:
        print("开始写入的值，",i)
        q.put(i)
        sleep(1)
def read(q):
    #for i  in range(q.qsize()):
    while not q.empty():
        print("正在读取的值：",q.get())
        time.sleep(1)

if __name__ == '__main__':
    
    q =Manager().Queue()

    pool = Pool(3)
    pool.apply(write,(q,))
    pool.apply(read,(q,))

    pool.close()
    pool.join()


```

