from multiprocessing import Queue
from multiprocessing import Process,Pool,Manager
from time import sleep

def writeq(q):
    a = ['a',
         'b',
         'c',
         'd']
    for i in a:
        print("开始写入：%s" %i)
        q.put(i)
        # sleep(1)

def readq(q):
    sleep(3)
    for i in range(q.qsize()):
        print("开始读取")
        res=q.get()
        print("读取的值为:",res)

if __name__ == '__main__':
    # q = Queue()
    # p1= Process(target=writeq,args=(q,))
    # p2 = Process(target=readq,args=(q,))
    # p1.start()
    # p2.start()
    # # p1.join()
    # # p2.join()

    q = Manager().Queue()
    pool = Pool(3)

    pool.apply_async(writeq,(q,))
    pool.apply_async(readq,(q,))

    pool.close()
    pool.join()