# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-11-25 17:40
python 函数的参数默认值只会在函数定义阶段被创建一次，之后不论再调用多少次，函数内拿到的默认值都是同一个对象。
"""
def append_value(value ,items = []):
    """向items列表中追加内容，并返回列表"""
    print(id(items))
    items.append(value)
    return items

print(append_value('foo'))
print(append_value('bar'))
print(append_value.__defaults__)