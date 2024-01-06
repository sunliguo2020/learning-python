# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-24 22:32
"""
from collections.abc import Iterable
from collections.abc import Iterator


class Range7:
    """
    生成某个范围内可被7整除或者包含7的整数
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        # 使用current保存当前所处的位置
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            # 当已经到达边界时，抛出异常终止迭代
            if self.current >= self.end:
                raise StopIteration
            if self.num_is_valid(self.current):
                ret = self.current
                self.current += 1
                return ret
            self.current += 1

    @staticmethod
    def num_is_valid(num):
        """判断数字是否满足要求"""
        if num == 0:
            return False
        return num % 7 == 0 or '7' in str(num)


class Myinter:
    def __iter__(self):
        return iter([])

    # def __next__(self):
    #     return True


if __name__ == '__main__':
    r = Range7(0, 20)
    print(r.current)
    for num in r:
        print(num)
    print(r.current)

    print(dir(r.__dict__))

    print(f"r 是否是可迭代对象{isinstance(r, Iterable)}")
    print(f"r 是否是迭代器{isinstance(r, Iterator)}")

    # a = Myinter()
    # print(iter(a))
