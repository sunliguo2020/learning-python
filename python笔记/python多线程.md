在一个进程中可以包含多个线程，多个线程共享一块内存空间



```python
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
```

### 多线程

有两种方法来创建线程：一种是继承threading.Thread类，并重写它的run()方法；

实例化threading.Thread对象的时候，将线程要执行的任务函数作为参数传入线程。



第一种写法：

Thread(group =None,target=None,name = None,args=(),kwargs={})

start() 启动线程

run()

isAlive()

getName()

```python
from threading import Thread

def func(name):
    print(f"我是{name}")

if __name__ == '__main__':
    t1 = Thread(target=func,args=("周杰伦",))
    t2 = Thread(target=func,args=("周润发",))
    t3 = Thread(target=func,args=("王力宏",))
    t1.start()
    t2.start()
    t3.start()
```

第二种写法（面向对象）：

```python
from threading import Thread

class Mythread(Thread):
    def __init__(self,name):
        super(Mythread,self).__init__()
        self.name = name
    def  run(self) :
        for i in range(100):
            print(self.name,i)
if __name__ == '__main__':
    t1 = Mythread('周杰伦')
    t2 = Mythread('王富贵')
    t3 = Mythread('王力宏')

    t1.start()
    t2.start()
    t3.start()
```

```python
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

```



对于Thread类，它的定义如下：

```python
threading.Thread(self, group=None, target=None, name=None,args=(), kwargs=None, *, daemon=None)
```

- 参数group是预留的，用于将来扩展；
- 参数target是一个可调用对象，在线程启动后执行；
- 参数name是线程的名字。默认值为“Thread-N“，N是一个数字。
- 参数args和kwargs分别表示调用target时的参数列表和关键字参数。

Thread类定义了以下常用方法与属性：

| 方法与属性                 | 说明                                                         |
| -------------------------- | ------------------------------------------------------------ |
| start()                    | 启动线程，等待CPU调度                                        |
| run()                      | 线程被cpu调度后自动执行的方法                                |
| getName()、setName()和name | 用于获取和设置线程的名称。                                   |
| setDaemon()                | 设置为后台线程或前台线程（默认是False，前台线程）。如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止。如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程执行完成后，程序才停止。 |
| ident                      | 获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None。 |
| is_alive()                 | 判断线程是否是激活的（alive）。从调用start()方法启动线程，到run()方法执行完毕或遇到未处理异常而中断这段时间内，线程是激活的。 |
| isDaemon()方法和daemon属性 | 是否为守护线程                                               |
| join([timeout])            | 调用该方法将会使主调线程堵塞，直到被调用线程运行结束或超时。参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。 |

### 线程池

第一种：

```python
from concurrent.futures import ThreadPoolExecutor


def func(name,t):
    for i  in range(10):
        print("我是", name)
    return name


def fn(res):
    print(res.result())


if __name__ == '__main__':
    #参数为线程池的大小，
    with ThreadPoolExecutor(3) as t:
        for i in range(100):
            t.submit(func, f"周杰伦{i}", 2).add_done_callback(fn)
         #t.sumit().add_done_callback()返回即执行add_done_callback()
         #返回callback执行的顺序是不确定的，返回值的顺序是不确定的
         
        result = t.map(func,['周杰伦'，'王力宏'],[1,2])
        print(result)
        for r in result:
            print(r)

```

第二种：

Pool([numprocess[,initializer[,initargs]]])

numprocess 进程个数（默认：cpu_cout())

```python
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
#pool.apply_async(get_request,urls,[1,2,3])
pool.map(get_request,urls,[1,2,3])
#get_request函数调用次数取决于urls列表元素的个数
#get_request 每次执行都会接受urls列表中的一个元素作为参数

print("总耗时；",time.time()-start)
pool.close()#进程池关闭后不再接受新的请求。
#调用join之前，先调用close函数，否则报错
#执行完close后不会再有新的进程加入到pool，join函数等待所有的子进程结束
pool.join()
```

## 队列Queue

Queue（block，timeout）