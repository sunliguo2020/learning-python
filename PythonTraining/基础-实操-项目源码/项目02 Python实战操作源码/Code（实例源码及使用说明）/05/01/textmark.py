# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/9  9:44 
# 文件名称   ：textmark.PY
# 开发工具   ：PyCharm
'''
  如何批量为图片添加文字水印
'''
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

path = input('请输入要添加水印的图片所在路径：')
text = input('请输入水印文字：')
positionflag = int(input('请输入水印位置（0：左上角，1：左下角，2：右上角，3：右下角，4：居中）：'))
alphavalue = float(input('请输入水印透明度（范围在0——1之间的1位小数）：'))
# 设置所使用的字体
font = ImageFont.truetype(r'simkai.ttf', 24)


# 文字水印
def textMark(img):
    try:
        im = Image.open(img).convert('RGBA')  # 打开原始图片，并转换为RGB
        newImg = Image.new('RGBA', im.size, (255, 255, 255, 0))  # 存储添加水印后的图片
        imagedraw = ImageDraw.Draw(newImg)  # 创建绘制对象
        imgwidth, imgheight = im.size  # 记录图片大小
        txtwidth = font.getsize(text)[0]  # 获取字体宽度
        txtheight = font.getsize(text)[1]  # 获取字体高度

        # 设置水印文字位置
        if positionflag == 0:  # 左上角
            position = (0, 0)
        elif positionflag == 1:  # 左下角
            position = (0, imgheight - txtheight)
        elif positionflag == 2:  # 右上角
            position = (imgwidth - txtwidth, 0)
        elif positionflag == 3:  # 右下角
            position = (imgwidth - txtwidth, imgheight - txtheight)
        elif positionflag == 4:  # 居中
            position = (imgwidth / 2, imgheight / 2)
        # 绘制文字
        imagedraw.text(position, text, font=font, fill="red")
        # 设置透明度
        alpha = newImg.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(alphavalue)
        newImg.putalpha(alpha)
        Image.alpha_composite(im, newImg).save(img, 'png')  # 保存图片
    except Exception as e:
        print(e)


import os

try:
    list = os.listdir(path)  # 遍历选择的文件夹
    for i in range(0, len(list)):  # 遍历文件列表
        filepath = os.path.join(path, list[i])  # 记录遍历到的文件名
        if os.path.isfile(filepath):  # 判断是否为文件
            filetype = os.path.splitext(filepath)[1]  # 获取扩展名
            if filetype == '.png':  # 判断是否为.png
                textMark(filepath)  # 批量添加文字水印
    print('批量添加水印完成')
except:
    print('请输入一个有效路径……')
