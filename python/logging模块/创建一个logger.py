# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-05 21:27
"""
import logging

# 创建一个文件处理程序并设置编码为UTF-8
file_handler = logging.FileHandler(filename='Camera.log', encoding='utf-8')

# 配置日志格式和级别
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
file_handler.setLevel(logging.DEBUG)

# 创建一个 logger 实例
logger = logging.getLogger('CameraLog')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
