# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/26 21:41
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
mitmdump -q -p 8888 -s v1.py
"""
from mitmproxy import http
from mitmproxy.http import Request


def request(flow: http.HTTPFlow):
    """

    @param flow:
    """
    flow.request.url = 'http://blog.sunliguo.com'
    print('请求->', flow.request.url)


def response(flow: http.HTTPFlow):
    """

    @param flow:
    """
    pass
