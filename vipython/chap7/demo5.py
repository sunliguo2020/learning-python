# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/12 18:09
"""


scores = {'张三':100,'李四':98,"王五":45}

for item in scores:
    print(item,scores[item],scores.get(item))