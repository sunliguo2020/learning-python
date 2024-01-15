# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/15 18:54
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 3、识别.py
 @Project : learning-python
"""
import requests
import ddddocr

# 验证码图片 url
code_url = 'https://xuexi.chinabett.com/Login/GetValidateCode/1705316148149'
res = requests.get(code_url)

# 保存截图
with open('code.jpg', 'wb') as fp:
    fp.write(res.content)

# 识别
ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)
