# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/8 11:15
输出100到999之间的水仙花数
"""

for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100

    # print(item,ge,shi,bai)
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print(item)
