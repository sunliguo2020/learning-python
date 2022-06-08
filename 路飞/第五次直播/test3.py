# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/21 18:45
"""

import time
from multiprocessing import Process


def get_request(url):
    print("正在请求网址的数据：", url)
    time.sleep(2)
    print("请求结束", url)


if __name__ == "__main__":
    start = time.time()
    urls = ['www.1.com',
            "www.2.com",
            "www.3.com"]
    for url in urls:
        # get_request(url)
        p = Process(target=get_request, args=(url,))
        p.start()
    print("总耗时：", time.time() - start)
