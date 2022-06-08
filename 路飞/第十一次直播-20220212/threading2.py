# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/17 12:34
"""
import requests
import time
from threading  import Thread
start = time.time()
urls = ['http://127.0.0.1:5000/bobo',
        'http://127.0.0.1:5000/tom',
        'http://127.0.0.1:5000/jay']


def get_request(url):
    """

    :param url:
    :return:
    """
    page_text = requests.get(url=url).text
    print(len(page_text))
ts = []

for url in  urls:
    t = Thread(target=get_request,args=(url,))
    ts.append(t)
    t.start()

for t in ts:
    t.join()

print("总耗时：",time.time()-start)