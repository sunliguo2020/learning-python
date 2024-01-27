# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/26 21:41
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : v1.py
 @Project : learning-python
"""
from mitmproxy import http
from mitmproxy.http import Request


def request(flow: http.HTTPFlow):
    """

    @param flow:
    """
    print('请求->', flow.request.url)


def response(flow: http.HTTPFlow):
    """

    @param flow:
    """
    pass
