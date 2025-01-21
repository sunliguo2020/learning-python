# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-04-11 12:45
"""
import logging

import requests
from lxml import etree

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def login(login_url=None):
    """

    Returns:

    """
    if login_url is None:
        login_url = 'http://192.168.1.21/users/login/'
    # 请求头
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
    }

    # 获取token
    session = requests.Session()
    r = session.get(login_url, headers=my_headers)
    # print(r.content)
    # print(r.text)
    # logger.debug(r)
    # /html/body/div/form/input
    # <input type="hidden" name="csrfmiddlewaretoken" value="eauvVaWq97BSlO58zzJnRkpOWboel1YoJNRudzX5YGsYkiLQZOm42oYu3M5UeW5E">
    html = etree.HTML(r.text)
    csrftoken = html.xpath("/html/body/div/section/form/input/@value")
    # print("csrftoken:", csrftoken)
    post_data = {
        'csrfmiddlewaretoken': csrftoken,
        'username': 'sunliguo',
        'password': 'tongmingao'
    }

    # 登录后
    r = session.post(login_url, headers=my_headers, data=post_data)
    # print(r.text)
    # print(r.cookies)
    # print(session.get('http://192.168.1.21/user/findbytoken/list/').text)

    return session


if __name__ == '__main__':
    print(login('http://127.0.0.1:8000/account/login/'))
