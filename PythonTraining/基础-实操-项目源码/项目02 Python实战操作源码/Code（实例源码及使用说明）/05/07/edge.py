# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：edge.PY
# 开发工具   ：PyCharm
'''
  图片的边界增强效果显示
'''
from PIL import Image,ImageFilter
img=Image.open('test.jpg') # 打开图片文件
newimg=img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 设置图片筛选器
newimg.save('边界增强.png', 'png') # 保存边界增强效果的图片