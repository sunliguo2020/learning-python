from multiprocessing import Queue

if __name__ == '__main__':

    q = Queue(3)
    q.put("消息1")
    q.put("消息2")
    q.put("消息3")
    q.put("消息4",block=True,timeout=1)