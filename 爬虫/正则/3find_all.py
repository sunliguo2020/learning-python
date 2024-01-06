# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 16:04
"""
import re

# findall 匹配所有 返回列表

print(re.findall('\d', '1234abc123'))

print(re.findall('\d', 'abc'))

print(re.findall('\d{2}', '123456abc789'))

myStr = '<div>我是HTML标签</div><div>div标签</div><div></div>'

# 匹配除div标签中的内容
print(re.findall('<div>.*?</div>', myStr))
print(re.findall('<div>.*</div>', myStr))

print(re.findall('<div>.+?</div>', myStr))
print(re.findall('<div>.+</div>', myStr))

# 存储括号中的值
print(re.findall('<div>(.*?)</div>', myStr))
