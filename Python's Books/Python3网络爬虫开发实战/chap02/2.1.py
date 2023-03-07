# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-27 9:46
"""
import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(type(response))  # <class 'http.client.HTTPResponse'>
# print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
