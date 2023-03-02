# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/12 7:19
"""
scores = {'张三':100,'李四':98,"王五":45}

print('张三' in scores)
del scores['张三']
print(scores)
#scores.clear()
scores['陈六']=33
print(scores)