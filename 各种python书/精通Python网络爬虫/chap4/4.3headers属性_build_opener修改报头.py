# -*- coding: utf-8 -*-
"""
 @Time : 2022/7/10 9:14
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 4.3headers属性_build_opener修改报头.py
 @Project : github
"""
import urllib.request
url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1;WOW64")

opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
print(data)