from concurrent.futures import ProcessPoolExecutor
from time import sleep
from random import randint

def fn(arg1,arg2,arg3=''):
   #sleep(arg1)
    sleep(arg1)
    print("arg1=",arg1)
    print("arg2=",arg2)
    print("arg3=",arg3)


if __name__ == '__main__':

    with ProcessPoolExecutor(3) as p:
        for i in range(1000):
            p.submit(fn,randint(0,10),i,{"key1":"sunliguo"})