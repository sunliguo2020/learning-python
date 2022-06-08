# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/8 16:16
"""
import requests

url = 'http://www.xinfadi.com.cn/getPriceData.html'
data = {'limit' : '20',
        'current' : '1',
        'pubDateStartTime' : '',
        'pubDateEndTime' : '',
        'prodPcatid' : '',
        'prodCatid' : ''
}
page = requests.post(url=url,data=data)

print(page.text)
with open('xinfadi-caiji.html', 'w', encoding='utf-8') as fp:
    fp.write(page.text)
