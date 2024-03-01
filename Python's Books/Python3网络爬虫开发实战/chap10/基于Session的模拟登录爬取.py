# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/21 12:23
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

session = requests.Session()
response_login = session.post(url=LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
}, allow_redirects=False)

cookies = session.cookies
print("cookies", cookies)

response_index = session.get(INDEX_URL)

print('Response Status', response_index.status_code)
print('Response Url', response_index.url)
