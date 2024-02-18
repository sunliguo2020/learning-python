# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/15 21:50
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import ddddocr

with open("fg.png", mode='rb') as f:
    slice_bytes = f.read()
with open('bg.jpg', mode='rb') as f:
    bg_bytes = f.read()

slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
res = slide.slide_match(slice_bytes, bg_bytes, simple_target=True)
x1, y1, x2, y2 = res['target']
print(x1)
