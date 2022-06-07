# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/8 11:56
"""
for i in range(5):
    for j in range(1,11):
        if j%2 == 0:
            continue
        print(j,end='\t')
    print()
