# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/9/8 20:49
"""
#json数据的存储

import json

s = '{"name":"张三"}'
#将字符串转为 字典对象
obj = json.loads(s)
print(type(obj))
print(obj)

#对象转为字符串

ss = json.dumps(obj,ensure_ascii=False)
print(type(ss))
print(ss)

#把对象（dict）保存到文件中
json.dump(obj,open('move.txt','w',encoding='utf-8'),ensure_ascii=False)

#把文件中的内容读取到python中
obj2 = json.load(open('move.txt',encoding='utf-8'))
print(type(obj2))
print(obj2)