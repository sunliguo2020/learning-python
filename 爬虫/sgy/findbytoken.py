# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-25 7:45
批量查询用户信息
"""
import logging

import requests
from lxml import etree

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def login():
    """

    Returns:

    """
    login_url = 'http://192.168.1.21/users/login/'
    # 请求头
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
    }

    # 获取token
    sss = requests.Session()
    r = sss.get(login_url, headers=my_headers)
    # print(r.content)
    # print(r.text)
    logger.debug(r)
    # /html/body/div/form/input
    # <input type="hidden" name="csrfmiddlewaretoken" value="eauvVaWq97BSlO58zzJnRkpOWboel1YoJNRudzX5YGsYkiLQZOm42oYu3M5UeW5E">
    html = etree.HTML(r.text)
    csrftoken = html.xpath("/html/body/div/form/input/@value")
    print(csrftoken)
    post_data = {
        'csrfmiddlewaretoken': csrftoken,
        'username': 'admin',
        'password': '!@#qweasd'
    }

    # 登录后
    r = sss.post(login_url, headers=my_headers, data=post_data)
    # print(r)
    # print(r.cookies)
    print(sss.get('http://192.168.1.21/user/findbytoken/list/').text)

    return sss


def get_phone(txt):
    with open(txt) as fp:
        for item in fp:
            yield item.strip()


def findbytoken(phone):
    """
    查询用户信息
    @param phone:   手机号码
    @return:    None
    """
    login_url = 'http://192.168.1.21/users/login/'
    # 请求头
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
    }

    # 获取token
    sss = requests.Session()
    r = sss.get(login_url, headers=my_headers)

    logger.debug(r)
    # /html/body/div/form/input
    # <input type="hidden" name="csrfmiddlewaretoken" value="eauvVaWq97BSlO58zzJnRkpOWboel1YoJNRudzX5YGsYkiLQZOm42oYu3M5UeW5E">
    html = etree.HTML(r.text)
    csrftoken = html.xpath("/html/body/div/form/input/@value")
    print(csrftoken)
    post_data = {
        'csrfmiddlewaretoken': csrftoken,
        'username': 'admin',
        'password': '!@#qweasd'
    }

    # 登录后
    r = sss.post(login_url, headers=my_headers, data=post_data)

    url = 'http://192.168.1.21/user/findbytoken/list/'
    rep = sss.get(url)
    html = etree.HTML(rep.text)
    csrftoken = html.xpath("//form/input/@value")
    print(csrftoken)
    post_data = {
        'csrfmiddlewaretoken': csrftoken,
        'phone': phone
    }
    post_url = 'http://192.168.1.21/user/findbytoken/create/'
    req = sss.post(post_url, data=post_data, cookies=rep.cookies)
    print(req.text)


if __name__ == '__main__':
    # login()
    phone = get_phone(r"d:\phone.csv")
    # print(phone)
    for count, item in enumerate(phone):
        if count < 0:
            continue
        print(f"{count}:{item}")
        # print(len(item))
        findbytoken(item)
