# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/24 10:47
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import execjs
import json

item = {
    'name': '凯文-杜兰特',
    'image': 'durant.png',
    'birthday': '1988-09-29',
    'height': '208cm',
    'weight': '108.9KG'
  }
file = 'crypto.js'
node = execjs.get()
ctx = node.compile(open(file).read())

js = f"getToken({json.dumps(item, ensure_ascii=False)})"
print(js)
result = ctx.eval(js)
print(result)
