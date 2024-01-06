# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 13:15
"""


def generator_test():
    while True:
        print('----1----')
        num = yield 100
        print('----2----', "num=", num)


if __name__ == '__main__':
    g = generator_test()
    print(next(g))
    print(next(g))
    print(next(g))

    print(g.send(11))
    print(g.send(12))