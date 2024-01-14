# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-14 14:37
"""
import requests
from bs4 import BeautifulSoup
url = 'https://passport.china.com/logon'
res = requests.post(url,
                    data={
                        # "userName": "15131255089",
                        "userName": "15131255089",
                        "password": "qwe123456"
                    },
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                        'Referer': 'https://passport.china.com/logon',
                        'Host': 'passport.china.com',
                        "X-Requested-With": "XMLHttpRequest"
                    })
cookie_dict = res.cookies.get_dict()
print(cookie_dict)
print(res.text)
new_main  = 'https://passport.china.com/main'
res = requests.get(new_main, cookies=cookie_dict)
soup = BeautifulSoup(res.text, features='html.parser')
tag = soup.find('p',attrs={'id':'usernick'})
print(tag.text)
print(tag.attrs['title'])
# print(res.text)
