# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：qrcodeinimg.PY
# 开发工具   ：PyCharm
'''
  如何生成仿微商的带二维码商品图片
'''
from PIL import Image

backpath=input('请输入商品图片路径：')
qrcodepath=input('请输入二维码图片路径：')
size=input('请输入您期望的二维码显示大小(逗号分隔)：').split(',')
width,height=(int(size[0]),int(size[1]))
backimg = Image.open(backpath) # 打开商品图片
qrcodeimg = Image.open(qrcodepath)  # 打开二维码图片
rgbaback = backimg.convert('RGBA')  # 将商品图片转换为RGBA
rgbaqrcode = qrcodeimg.convert('RGBA')  # 将水印图片转换为RGBA
imgwidth, imgheight = rgbaback.size  # 获取商品图片尺寸
# 缩放二维码图片
rgbaqrcode = rgbaqrcode.resize((width,height), resample=Image.ANTIALIAS)
position = (imgwidth - width, imgheight - height) # 设置二维码位置为右下角
rgbaback.paste(rgbaqrcode, position)  # 在指定位置添加二维码图片
rgbaback.save(backpath)  # 保存加二维码后的商品图片
