# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-23 20:27
"""
import re

result = re.findall('a', 'adfasfa')
print(result)
result = re.findall(r'\d','我今年18岁，我有200000块')
print(result)
result = re.findall(r'\d?','我今年18岁，我有200000块')
print(result)
result = re.findall(r'\d+','我今年18岁，我有200000块')
print(result)

result = re.finditer(r'\d+','我今年18岁，我有200000块')

for item in result:
    print(item)
    print(item.group())

# 预加载
obj = re.compile(r"\d+")
result = obj.findall('我叫周杰伦，今年32岁，我的班级是5年级3班')
print(result)

# 想要提取数据必须用小括号括起来，可以单独起名字
# (?P<名字>正则)
# 提取数据的时候，需要 group("名字")
s = """
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='西游记'><span id='10016'>中国移动</span></div>
"""
# obj = re.compile(r"<span id='\d+'>.*?</span>") # ["<span id='10010'>中国联通</span>", "<span id='10016'>中国移动</span>"]

# obj = re.compile(r"<span id='(\d+)'>(.*?)</span>") # [('10010', '中国联通'), ('10016', '中国移动')]
obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")

result = obj.findall(s)
print(result)

result = obj.finditer(s)
for item in result:
    print(item.group("id"))
    print(item.group("name"))