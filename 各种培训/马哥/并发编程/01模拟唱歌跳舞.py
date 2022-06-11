# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 7:06
"""
from time import sleep


def sing():
    for i in range(3):
        print("正在唱歌---")
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞---")
        sleep(1)

if __name__ == '__main__':
    sing()
    dance()