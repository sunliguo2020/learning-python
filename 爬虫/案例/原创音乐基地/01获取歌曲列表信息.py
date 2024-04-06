# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/28 21:24
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from urllib.parse import urljoin

import requests
from lxml import etree

base_url = 'https://5sing.kugou.com/yc/list?t=2&l=&s=&p=1'

resp = requests.get(base_url)
# print(resp.text)

page = resp.text
html = etree.HTML(page)

dl_list = html.xpath('//div[@class="lists"]/dl')

# 遍历所有的标签
for dl in dl_list:
    title = dl.xpath('.//h3/a/text()')[0]

    music_url = urljoin(base_url, dl.xpath('.//h3/a/@href')[0])

    music_id = dl.xpath('.//a[@class="m_date_shou"]/@argid')[0]

    print(title, '-', music_url, music_id)
