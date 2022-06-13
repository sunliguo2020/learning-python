# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/4/20 17:54
"""
import json
json_data = open('../data/chp3/data-text.json','rb').read()
data =json.loads(json_data)
print(type(data))
'''
for item in data:
    print(item)'''