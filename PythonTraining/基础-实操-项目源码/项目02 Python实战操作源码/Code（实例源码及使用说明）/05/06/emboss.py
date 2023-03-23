# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：emboss.PY
# 开发工具   ：PyCharm
'''
  图片的浮雕效果显示
'''
from PIL import Image,ImageFilter
img=Image.open('test.jpg') # 打开图片文件
newimg=img.filter(ImageFilter.EMBOSS) # 设置图片筛选器
newimg.save('浮雕效果.png', 'png') # 保存浮雕效果的图片