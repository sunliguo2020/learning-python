# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/4 21:32
"""
import os
import urllib
import urllib.request

import requests
from lxml import etree


def down_jd_pic(base_url):
    """
    下载单页面的手机图片
    @param base_url:
    @return:
    """
    # base_url = 'https://list.jd.com/list.html?cat=9987,653,655'

    jd_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    resp = requests.get(url=base_url, headers=jd_headers)
    # print(resp.text)
    tree = etree.HTML(resp.text)
    # print(type(tree))
    li_list = tree.xpath('//ul[@class="gl-warp clearfix"]/li')
    for li in li_list:
        """
        <img width="220" height="220" data-img="1" data-lazy-img="//img12.360buyimg.com/n7/jfs/t1/111789/21/25219/92851/6246a22dEe36375a5/fbf44bf375a9e447.jpg" source-data-lazy-img="">
        """
        jd_phone_pic = li.xpath('.//div[@class="p-img"]/a/img/@data-lazy-img')[0]  #
        # print(li.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img/@src'))
        jd_phone_pic = urllib.parse.urljoin(base_url, jd_phone_pic)

        print(jd_phone_pic)
        # urllib.request.urlretrieve(jd_phone_pic,filename=f"{os.path.basename(jd_phone_pic)}")
        with open("pic\\" + f"{os.path.basename(jd_phone_pic)}", 'wb') as f:
            content = requests.get(jd_phone_pic, headers=jd_headers).content
            f.write(content)


if __name__ == '__main__':
    for page in range(11, 95):
        url = f'https://list.jd.com/list.html?cat=9987%2C653%2C655&page={page}&s=57&click=0'
        print(url)
        down_jd_pic(url)
