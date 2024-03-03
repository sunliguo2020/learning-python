# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/3 10:50
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import json

import execjs
import requests

headers = {
    'authority': 'api.zzzmh.cn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://bz.zzzmh.cn',
    'pragma': 'no-cache',
    'referer': 'https://bz.zzzmh.cn/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
}


def getPageData(page):
    """
    获取每页的加密数据
    @param page:
    @return:
    """
    json_data = {
        'size': 24,
        'current': page,  # 页码
        'sort': 0,
        'category': 0,
        'resolution': 4,  # 分辨率
        'color': 0,
        'categoryId': 0,
        'ratio': 0,
    }

    response = requests.post('https://api.zzzmh.cn/bz/v3/getData', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"size":24,"current":2,"sort":0,"category":0,"resolution":0,"color":0,"categoryId":0,"ratio":0}'
    # response = requests.post('https://api.zzzmh.cn/bz/v3/getData', headers=headers, data=data)

    return response.json().get('result')


# js解密函数
def jiemi(data):
    with open('./demo.js', encoding="utf-8") as fp:
        js_code = fp.read()
    js_str = execjs.compile(js_code).call('jiemi', data)
    return json.loads(js_str)


# 解密url地址
def parse(data):
    baseUrl = 'https://api.zzzmh.cn/bz/v3/getUrl/'
    if data.get('t') == '1':
        suffix = '10'
    elif data.get('t'):
        suffix = '20'

    return baseUrl + data.get('i') + suffix


if __name__ == '__main__':
    # jiaMiData = getPageData(1)
    # print(jiemi(jiaMiData))
    for page in range(1, 11):
        print(f'开始下载第{page}页的壁纸')
        data = getPageData(page)
        # 解密数据
        img_list = jiemi(data).get('list')

        # 开始下载
        for item in img_list:
            image_url = parse(item)
            print(image_url)
            image_name = item.get('i') + '.jpg'
            # 跳转后的 新地址
            resp = requests.get(image_url)
            # print(resp.url)

            # 去掉后面的 thumbs
            new_url = resp.url.split('/thumbs')[0]
            print(new_url)

            # 保存图片

            with open(image_name, 'wb') as fp:
                fp.write(requests.get(new_url).content)
            # break
