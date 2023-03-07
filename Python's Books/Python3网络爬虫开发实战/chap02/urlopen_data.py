# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-27 9:53
POST /post HTTP/1.1
Accept-Encoding: identity
Content-Type: application/x-www-form-urlencoded
Content-Length: 11
Host: www.httpbin.org
User-Agent: Python-urllib/3.10
Connection: close

name=germeyHTTP/1.1 200 OK
Date: Fri, 27 Jan 2023 02:22:49 GMT
Content-Type: application/json
Content-Length: 459
Connection: close
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "name": "germey"
  },
  "headers": {
    "Accept-Encoding": "identity",
    "Content-Length": "11",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "www.httpbin.org",
    "User-Agent": "Python-urllib/3.10",
    "X-Amzn-Trace-Id": "Root=1-63d33579-33b5fd383e7efad547a490df"
  },
  "json": null,
  "origin": "223.97.151.137",
  "url": "http://www.httpbin.org/post"
}
"""
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'name': 'germey', 'age': 18}), encoding='utf-8')
print(data)
print(type(data))
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
response = urllib.request.urlopen('https://www.httpbin.org/post', data='a=12'.encode('utf-8'))
print(type('a=12'.encode('utf-8')))
print(response.read().decode('utf-8'))
