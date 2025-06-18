# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-04-11 17:49
"""
import os
from lxml import etree

from login import login

BASE_HOST = '192.168.1.21'
# BASE_HOST = '127.0.0.1:8000'


def yield_idcard(idcard_txt=r'd:\valid_ids.txt'):
    """
    @param idcard_txt: 身份证号文件路径
    @return: 身份证号生成器
    """
    if not os.path.exists(idcard_txt):
        raise FileNotFoundError(f'文件不存在：{idcard_txt}')
    with open(idcard_txt) as fp:
        for idcard in fp:
            yield idcard.strip()


def hisifo_spider(idcard, year):
    """

    @param idcard: 身份证号
    @param year: 年份
    @return:
    """
    # 获取csrftoken的url
    get_url = f'http://{BASE_HOST}/healthcare/hisinformation/index/'
    # 查询数据的url
    post_url = f'http://{BASE_HOST}/healthcare/hisinformation/spider/'

    r = session.get(get_url)
    html = etree.HTML(r.text)
    csrftoken = html.xpath("/html/body/div/div[1]/form/input[1]/@value")

    post_data = {
        'csrfmiddlewaretoken': csrftoken,
        'idcard': idcard,
        'year': year
    }
    resp = session.post(post_url, data=post_data, allow_redirects=False)


def personal_spider(idcard):
    """

    """
    get_url = f'http://{BASE_HOST}/healthcare/personaldoc/index/'
    post_url = f'http://{BASE_HOST}/healthcare/personaldoc/spider/'

    r = session.get(get_url)
    html = etree.HTML(r.text)
    csrftoken = html.xpath("/html/body/div[1]/form/input[1]/@value")

    post_data = {
        'csrfmiddlewaretoken': csrftoken,
        'idcard': idcard,
    }
    resp = session.post(post_url, data=post_data, allow_redirects=False)


if __name__ == '__main__':
    session = login(f'http://{BASE_HOST}/account/login/')
    for no, idcard in enumerate(yield_idcard()):
        if no > 0:
            print(no, ':', idcard)
            personal_spider(idcard)
            # hisifo_spider(idcard, 2021)
            # break
