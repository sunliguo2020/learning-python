# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/9  9:48 
# 文件名称   ：imgmark.PY
# 开发工具   ：PyCharm
'''

'''
from PIL import Image
path=input('请输入要添加水印的图片所在路径：')
imgpath=input('请输入要作为水印图片的路径：')
positionflag=int(input('请输入水印位置（0：左上角，1：左下角，2：右上角，3：右下角，4：居中）：'))
alphavalue=int(input('请输入水印透明度（范围在1——10之间）：'))

# 图片水印
def imgMark(img):
    im = Image.open(img) # 打开原始图片
    mark = Image.open(imgpath) # 打开水印图片
    rgbaim = im.convert('RGBA') # 将原始图片转换为RGBA
    rgbamark = mark.convert('RGBA') # 将水印图片转换为RGBA
    imgwidth, imgheight = rgbaim.size # 获取原始图片尺寸
    nimgwidth, nimgheight = rgbamark.size # 获取水印图片尺寸
    # 缩放水印图片
    scale = 10
    markscale = max(imgwidth / (scale * nimgwidth), imgheight / (scale * nimgheight))
    newsize = (int(nimgwidth * markscale), int(nimgheight * markscale)) # 计算新的尺寸大小
    rgbamark = rgbamark.resize(newsize, resample=Image.ANTIALIAS) # 重新设置水印图片大小
    nimgwidth, nimgheight = rgbamark.size # 获取水印图片缩放后的尺寸
    # 设置水印文字位置
    if positionflag == 0:  # 左上角
        position = (0, 0)
    elif positionflag == 1:  # 左下角
        position = (0, imgheight - nimgheight)
    elif positionflag == 2:  # 右上角
        position = (imgwidth - nimgwidth, 0)
    elif positionflag == 3:  # 右下角
        position = (imgwidth - nimgwidth, imgheight - nimgheight)
    elif positionflag == 4:  # 居中
        position = (int(imgwidth / 2), int(imgheight / 2))
    # 设置透明度：img.point(function)接受一个参数，且对图片中的每一个点执行这个函数，这个函数是一个匿名函数，使用lambda表达式来完成
    # convert()函数，用于不同模式图像之间的转换，模式“L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    # 在PIL中，从模式“RGB”转换为“L”模式是按照下面的公式转换的：L = R * 299/1000 + G * 587/1000+ B * 114/1000
    rgbamarkpha = rgbamark.convert("L").point(lambda x: x/alphavalue)
    rgbamark.putalpha(rgbamarkpha)
    # 水印位置
    rgbaim.paste(rgbamark, position, rgbamarkpha)
    rgbaim.save(img) # 保存水印图片

import os
try:
    list = os.listdir(path)  # 遍历选择的文件夹
    for i in range(0, len(list)):  # 遍历文件列表
        filepath = os.path.join(path, list[i])  # 记录遍历到的文件名
        if os.path.isfile(filepath):  # 判断是否为文件
            filetype = os.path.splitext(filepath)[1]  # 获取扩展名
            if filetype == '.png':  # 判断是否为.png
                imgMark(filepath) # 批量添加图片水印
    print('批量添加水印完成')
except Exception as e:
    print(e)