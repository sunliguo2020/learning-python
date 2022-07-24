# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/9/20 15:15
"""
import requests
import urllib.parse
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
def send_request():
    url = 'http%3A%2F%2Fshp%2Eqpic%2Ecn%2Fishow%2F2735052109%2F1590023062%5F84828260%5F20731%5FsProdImgNo%5F1%2Ejpg%2F200'
    url2 = urllib.parse.unquote(url)
    print(url2)

if __name__ == '__main__':
    send_request()