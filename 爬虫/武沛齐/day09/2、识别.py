# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-14 15:53
"""
import ddddocr
import requests

slice_bytes = requests.get("https://static.geetest.com/captcha_v4/e70fbf1d77/slide/1e8ffe6222/2022-04-21T09/bg/1117e757921d405c87280ad8de8bbdf1.png").content
bg_bytes = requests.get("https://static.geetest.com/captcha_v4/e70fbf1d77/slide/1e8ffe6222/2022-04-21T09/slice/1117e757921d405c87280ad8de8bbdf1.png").content


slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
res = slide.slide_match(slice_bytes, bg_bytes, simple_target=True)
x1, y1, x2, y2 = res['target']
print(x1, y1, x2, y2)  # 114 45 194 125