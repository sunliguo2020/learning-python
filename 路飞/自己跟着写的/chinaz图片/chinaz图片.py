# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/24 18:17
"""

from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue
from urllib import parse

import requests
from lxml import etree


def get_img_src(q):
    url = 'https://sc.chinaz.com/tupian/index.html'
    for i in range(1, 2654):
        url = f'https://sc.chinaz.com/tupian/index_{i}.html'
        print("正在提取：", url)
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        tree = etree.HTML(resp.text)
        div_list = tree.xpath('//div[@id="container"]//p/a[1]/@href')
        for detail_url in div_list:
            detail_url = parse.urljoin(url, detail_url)
            # print(detail_url)
            child_resp = requests.get(detail_url)
            child_resp.encoding = 'utf-8'
            child_tree = etree.HTML(child_resp.text)
            img_src = child_tree.xpath("//div[@class='imga']//img/@src")[0]

            src = parse.urljoin(url, img_src)
            q.put(src)
            print(f"把{src}放入队列")
    q.put('完事了')


def downlad(url):
    file_name = url.split('/')[-1]
    print("正在下载图片：", file_name)
    content = requests.get(url).content
    with open('./img/' + file_name, 'wb') as fp:
        fp.write(content)


def download_img(q):
    with ThreadPoolExecutor(10) as t:
        while True:
            url = q.get()
            if url == '完事了':
                break
            t.submit(downlad, url)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=get_img_src, args=(q,))
    p2 = Process(target=download_img, args=(q,))

    p1.start()
    p2.start()
