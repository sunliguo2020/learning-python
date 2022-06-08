# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/21 10:13
"""
import requests
def down_yy(page):
    """

    :param page:
    :return:
    """
    url = "https://api-tinyvideo-web.yy.com/home/tinyvideosv2"
    params = {"data": '{"uid":0,"page":'+str(page)+',"pageSize":10}'}
    # print(type(params))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers, params=params)
    # pprint.pprint(resp.json())
    # print(resp.url)
    json_data = resp.json()

    video_data = json_data['data']['data']
    for data in video_data:
        #print(data)
        resurl = data['resurl']
        yyNum = data['yyNum']
        video_res = requests.get(url=resurl,headers=headers).content
        print(resurl)
        with open("D:\yy\\"+str(yyNum)+'.mp4','wb') as fp:
            fp.write(video_res)

if __name__ == '__main__':
    for i in range(1,100):
        print(f"正在爬取{i}页数据")
        down_yy(i)