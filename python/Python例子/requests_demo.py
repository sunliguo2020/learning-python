# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/26 9:23
"""
import requests
url = "http://httpbin.org/post"
post_data = {"name":"sunliguo",
             "password":"A12345"}
header = {"User-Agent":"Mozilla /5.0"}
resp = requests.post(url=url,data=post_data,headers=header)
#print(resp.text)
"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "sunliguo", 
    "password": "A12345"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "29", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla /5.0", 
    "X-Amzn-Trace-Id": "Root=1-623e6c53-3e3bfd076e70c14f21642fba"
  }, 
  "json": null, 
  "origin": "112.224.67.153", 
  "url": "http://httpbin.org/post"
}

"""

url = 'http://httpbin.org/get'
resp = requests.get(url=url,params=post_data,headers=header)
print(resp.text)
"""
{
  "args": {
    "name": "sunliguo", 
    "password": "A12345"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla /5.0", 
    "X-Amzn-Trace-Id": "Root=1-623e6c7a-126e4a156f26486a155600db"
  }, 
  "origin": "112.224.67.153", 
  "url": "http://httpbin.org/get?name=sunliguo&password=A12345"
}

"""