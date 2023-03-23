# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/8  14:54 
# 文件名称   ：sketch.PY
# 开发工具   ：PyCharm
'''
  根据图片显示其轮廓
'''
from PIL import Image,ImageFilter
img=Image.open('test.png') # 打开图片文件
newimg=img.filter(ImageFilter.CONTOUR) # 设置图片筛选器
newimg.save('轮廓效果.png', 'png') # 保存轮廓效果的图片