# -*- coding: utf-8 -*-
"""
 @Time : 2023/3/5 10:51
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : open_test.py
 @Project : learning-python
"""
file_path = r'F:\eml\1fb2d55243191295e4752c4cf9acae8d.eml'
print(file_path)
with open(file_path) as fp:
    print(type(fp))
