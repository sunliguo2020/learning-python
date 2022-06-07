"""
测试全局变量和局部变量的效率

"""

import math
import time

def test01():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end=time.time()

    print("耗时：{0}".format(end-start))

test01()