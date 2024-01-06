# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 17:09
"""
import requests

headers = {
    'Referer': 'https://www.luffycity.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}

params = {
    'pid': '1704013505652X1145846',
    'device': 'desktop',
}

response = requests.get(
    'https://hw-dts.videocc.net/d1977c4d68/0/1660931458368/7/57/74/47_3/d1977c4d68e6de3169df7098c3577447_3_47.pts',
    params=params,
    headers=headers,
)

with open('1.mp4','wb') as f :
    f.write(response.content)