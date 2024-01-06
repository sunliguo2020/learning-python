# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 22:30
"""

import os.path
from multiprocessing import Pool

import requests
from lxml import etree

headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # # 'Cookie': '_agep=1704029659; _agfp=defbc757df5957fe8156b8cb5d55756a; _agtk=fef911d8e09c0db101ad9cf1cdbf084d; Hm_lvt_2fc12699c699441729d4b335ce117f40=1704029659; XSRF-TOKEN=eyJpdiI6ImFYaTR0WlhmZGYxWlFsWTBKTERheGc9PSIsInZhbHVlIjoiMUVRdkQrNUhVc1NWYnBOcnJIS29Fa0x1eE9ieENFcVFVdmtpa1dsNWMxUkhvZ3JESTMxT01PaWdOT2lWZ3YrcyIsIm1hYyI6Ijg2NjQ2ZmNjMjAxY2I3ZWYwZDQ5NTk5MGQ3ZjRjYzdlYzI0MGQ5YmE1MjEyY2Y5MTYzZGRiYmIyOWZiM2IwNDMifQ%3D%3D; doutula_session=eyJpdiI6IkZIU3NwTHBrTkxmdEFoU1FtVmdIREE9PSIsInZhbHVlIjoiWXZ2M0lkSHJNbEw0Q0NnQ2diYVVsMnJvc3F3VVpsOGMxRjFvOTdWcTRIWkI4NHlwU2FKTDZOOVNXMmZXYnd4NyIsIm1hYyI6Ijk4NDAwMGY2NDU3NTk3MDMzYzNmYzU4OWIxYWIxNjAxZDBlMTg3NmYxYmFhNTBiOWYwNjU5MjkzZmYzNjdjNDMifQ%3D%3D; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1704031216',
    # 'Pragma': 'no-cache',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'none',
    # 'Sec-Fetch-User': '?1',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    # 'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
}


def get_src(page):
    for i in range(1, page + 1):
        url = f'https://www.pkdoutu.com/article/list/?page={i}'
        print(f"正准备下载{url}的图片")
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        tree = etree.HTML(response.content)
        # img_list = tree.xpath('//img[@referrerpolicy="no-referrer"]/@data-original')
        img_list = tree.xpath('//@data-original')
        yield img_list


def download(url):
    img_name = os.path.basename(url)
    print(f'准备下载{url}')
    path = 'img'
    if not os.path.isdir(path):
        os.makedirs(path)
    with open(os.path.join(path, img_name), 'wb') as f:
        f.write(requests.get(url).content)


if __name__ == '__main__':

    p = Pool()
    for url_list in get_src(20):
        for url in url_list:
            p.apply_async(download, args=(url,))
    p.close()
    p.join()
