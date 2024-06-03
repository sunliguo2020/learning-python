# -*- coding: utf-8 -*-
"""
 @Time : 2024/6/2 9:40
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import os
from pathlib import Path

from PIL import Image


def trim_image(img_path, output_path):
    # 打开图片并获取其alpha通道（如果存在）
    img = Image.open(img_path)
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        # 图片有alpha通道或透明度信息
        datas = img.getdata()

        # 转换为RGBA模式（如果不是的话）
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            datas = img.getdata()

            # 初始化非透明像素的最小和最大x、y坐标
        x_min, y_min, x_max, y_max = float('inf'), float('inf'), -float('inf'), -float('inf')

        # 遍历每个像素
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b, a = datas[y * width + x]  # 获取RGBA值
                if a != 0:  # alpha值不为0
                    x_min, y_min = min(x, x_min), min(y, y_min)
                    x_max, y_max = max(x, x_max), max(y, y_max)

                    # 裁剪图片
        if x_min != float('inf') and y_min != float('inf') and x_max != -float('inf') and y_max != -float('inf'):
            box = (x_min, y_min, x_max + 1, y_max + 1)  # +1确保包括最后一个像素
            new_img = img.crop(box)
            new_img.save(output_path)
        else:
            print("没有找到非透明像素，图片可能是全透明的")
    else:
        # 图片没有透明部分，可以直接保存或处理
        img.save(output_path)


def process_directory(src_dir, dst_dir):
    # 确保目标目录存在
    Path(dst_dir).mkdir(parents=True, exist_ok=True)

    # 遍历源目录中的文件和子目录
    for root, dirs, files in os.walk(src_dir):
        # 计算相对于源目录的相对路径
        rel_path = os.path.relpath(root, src_dir)

        # 在目标目录中创建相应的目录结构
        dst_path = os.path.join(dst_dir, rel_path)
        Path(dst_path).mkdir(parents=True, exist_ok=True)

        # 遍历文件
        for file in files:
            # 检查是否是图片文件（这里只是示例，你可以添加更多的图片格式）
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
                # 构建源图片和目标图片的完整路径
                src_file_path = os.path.join(root, file)
                dst_file_path = os.path.join(dst_path, file)

                # 调用trim_image函数处理图片
                trim_image(src_file_path, dst_file_path)


if __name__ == '__main__':
    src_directory = '../pic'  # 源目录路径
    dst_directory = 'pic2'  # 目标目录路径

    # 假设trim_image函数已经定义好了
    process_directory(src_directory, dst_directory)
