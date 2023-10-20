# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-25 7:45
批量查询用户信息
"""
import requests
from lxml import etree


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
    url = 'http://192.168.1.21/user/findbytoken/list/'
    rep = requests.get(url)
    html = etree.HTML(rep.text)
    csrftoken = html.xpath("//form/input/@value")
    print(csrftoken)
    post_data = {
        'csrfmiddlewaretoken': csrftoken,
        'phone': phone
    }
    post_url = 'http://192.168.1.21/user/findbytoken/create/'
    req = requests.post(post_url, data=post_data, cookies=rep.cookies)
    # print(req.text)


if __name__ == '__main__':
    phone = get_phone(r"d:\phone.txt")
    # print(phone)
    for count, item in enumerate(phone):
        if count < 0:
            continue
        print(f"{count}:{item}")
        # print(len(item))
        findbytoken(item)
