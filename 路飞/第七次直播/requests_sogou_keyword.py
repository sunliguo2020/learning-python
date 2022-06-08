# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/29 16:48
"""

import requests
keyword = input('请输入关键词：')
pram = {
    'query':keyword
}
url = 'http://www.sogou.com/web'

head = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

response = requests.get(url= url,params=pram,headers=head)

page_text = response.text

file_name = keyword+'.html'

with open(file_name,'w',encoding='utf-8') as fp:
    fp.write(page_text)