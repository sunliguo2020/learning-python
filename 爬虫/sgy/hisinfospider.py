# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-04-11 17:49
"""
from lxml import etree

from login import login

BASE_HOST = '192.168.1.21'
# BASE_HOST = '127.0.0.1:8000'


def yield_idcard():
    with open(r'd:\tongxue.csv') as fp:
        for idcard in fp:
            yield idcard.strip()


def his_spider(idcard, year):
    get_url = f'http://{BASE_HOST}/healthcare/hisinformation/index/'
    post_url = f'http://{BASE_HOST}/healthcare/hisinformation/spider/'

    session = login(f'http://{BASE_HOST}/account/login/')

    r = session.get(get_url)
    html = etree.HTML(r.text)
    csrftoken = html.xpath("/html/body/div/div[1]/form/input[1]/@value")

    post_data = {
        'csrfmiddlewaretoken': csrftoken,
        'idcard': idcard,
        'year': year
    }
    resp = session.post(post_url, data=post_data, allow_redirects=False)
    # print(resp.text)


if __name__ == '__main__':
    for no, idcard in enumerate(yield_idcard()):
        # if idcard.startswith('3707831986'):
        #     print(no,':',idcard)
        #     # his_spider(idcard, 2023)
        #     # break
        if no > 0:
            print(no, ':', idcard)
            his_spider(idcard, 2023)
