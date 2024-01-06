# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-11-15 19:57
"""
# 1、目标网站
url = 'https://music.163.com/discover/toplist?id=3778678'
# 2、发送请求
import requests

headers = {
    "User-Agent": "Mozilla"
}
# 获取网页数据
res = requests.get(url, headers=headers)

from lxml import etree

html = etree.HTML(res.text)

id_list = html.xpath('//a[contains(@href,"/song?")]')
# 3、提取需要信息 保存
for data in id_list:
    # href = data.xpath('')
    music = data.xpath('./text()')
    if len(music)>0:
        music = music[0]
    else:
        continue
    print(music)
