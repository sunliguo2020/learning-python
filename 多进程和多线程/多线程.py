from threading import Thread


def func():
    for i in range(10000):
        print("func", i)
#
#
# t = Thread(target=func)
# t.start()
# t.join()
#
# for i in range(10):
#     print("main", i)

class MyThread(Thread):

    def __init__(self,func):
        # super.__init__()
        Thread.__init__(self)
        self.func = func

    def run(self):
        # for i in range(10000):

        #     print("thread", i)
        self.func()

t = MyThread(func)
t.start()
for i in range(10):
    print("main", i)
