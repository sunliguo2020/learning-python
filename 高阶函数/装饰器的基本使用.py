import time


def writeLog(fun):
    print("日期时间", time.asctime(), fun.__name__)


def funout(fun):
    def funIn():
        writeLog(fun)
        fun()

    return funIn


@funout
def fun1():
    print("功能1")


fun1()
