# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/26 9:31
"""
from concurrent.futures import ThreadPoolExecutor


def fun(arg1, arg2, arg3=''):
    print("我是函数fun")
    # print(f"正在休息{i}秒")
    # time.sleep(arg1)
    print("我的参数为：", arg1, arg2, arg3)

    return "我是返回值"


def fun2(res):
    print(res.result())


if __name__ == '__main__':
    with ThreadPoolExecutor(4) as executor:
        for i in range(1, 100):
            # def submit(*args, **kwargs):
            executor.submit(fun, i, i + 1, {"si": "123"}).add_done_callback(fun2)
