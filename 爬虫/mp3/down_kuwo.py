# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-15 21:47
"""
# 3.输入一首歌曲的地址（不是MP3地址），解析得到音乐,完整项目
import time
import requests

print("3.输入一首歌曲的地址（不是MP3地址），解析得到音乐")


def get_mp3_name():
    data_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())  # 格式化获取的当地时间
    mp3_name = data_time + ".mp3"
    return mp3_name


def downMusic(url):
    # 该网站有反爬机制，要模拟浏览器来进行伪装。
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
        'csrf': 'RUJ53PGJ4ZD',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD'
    }

    mid = url.split("/")[-1]  # 假设url是http://www.kuwo.cn/play_detail/196835141，得到mid196835141
    # 把得到的mid参数填入指定位置得到了存放MP3文件地址的json地址
    save_mp3_url = "http://www.kuwo.cn/api/v1/www/music/playUrl?mid=%s&type=mp3&httpsStatus=1&reqId=66231ca1-5e04-11ec-96d1-d1bbc17ab269" % mid
    mp3_response = requests.get(save_mp3_url, headers=headers)  # 解析存放MP3文件地址的json地址
    mp3_url = mp3_response.json().get("data").get("url")  # 根据解析存放MP3文件地址的json地址的内容，获取MP3地址
    with open(get_mp3_name(), "wb") as file:
        music = requests.get(mp3_url, headers=headers)  # 获取解析到的数据
        file.write(music.content)  # 把数据写入缓冲区文件
        file.flush()  # 把数据存入缓冲区
        file.close()  # 关闭文件


url = input("输入一首歌曲的播放地址下载歌曲:")
downMusic(url)
