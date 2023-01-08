# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-04 17:22
冒泡算法
"""
from random import shuffle

tmpList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(tmpList)
print(tmpList)

for i in range(len(tmpList)):
    print(f'i:{i}')
    for j in range(0, len(tmpList) - 1 - i):
        print(f'j:{j}')
        if tmpList[j] > tmpList[j + 1]:
            tmpList[j], tmpList[j + 1] = tmpList[j + 1], tmpList[j]
    print(tmpList)
