# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2026/3/17 8:48
"""
import os

# 【请在这里修改为你的文件夹路径】
folder_path = r"D:\桌面\新建文件夹"

# 遍历文件夹里的所有文件
for filename in os.listdir(folder_path):
    # 获取文件完整路径
    old_path = os.path.join(folder_path, filename)

    # 只处理文件，跳过文件夹
    if os.path.isfile(old_path):
        # 新文件名 = 原文件名 + .txt
        new_name = filename + ".txt"
        new_path = os.path.join(folder_path, new_name)

        # 重命名
        os.rename(old_path, new_path)

print("✅ 所有文件已批量添加 .txt 后缀！")