import requests  # 网络请求模块
import time      # 时间模块
import random    # 随机模块
import os        # 操作系统模块
import re        # 正则表达式
'''
获取json中的其它信息
'''

# 哔哩哔哩小视频json地址
json_url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={page}1&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'
class Crawl():
    def __init__(self):
        # 创建头部信息
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}

    def get_json(self,json_url):
        response = requests.get(json_url, headers=self.headers)
        # 判断请求是否成功
        if response.status_code == 200:
            return response.json()  # 返回json信息
        else:
            print('获取json信息的请求没有成功！')
if __name__ == '__main__':
    c = Crawl()
    for page in range(0,10):
        json = c.get_json(json_url.format(page=page))  # 获取返回的json数据
        infos = json['data']['items']  # 信息集
        for info in infos:             # 遍历信息
            title = info['item']['description']  # 视频标题
            upload_time =  info['item']['upload_time']  # 发布时间
            video_url = info['item']['video_playurl']  # 视频地址
            user_name = info['user']['name']  # 用户名称
            watched_num = info['item']['watched_num']  # 观看人数
            print('视频标题为：',title)      # 打印视频标题
            print('发布时间为：',upload_time)# 打印发布时间
            print('视频地址为：',video_url)  # 打印视频地址
            print('用户名称为：',user_name)  # 打印用户名称
            print('观看人数为：',watched_num)# 打印视频观看人数
        time.sleep(random.randint(3, 6))  # 随机产生获取json请求的间隔时间
