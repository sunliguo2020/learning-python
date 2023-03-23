import requests  # 网络请求模块
import time      # 时间模块
import random    # 随机模块
import os        # 操作系统模块
import re        # 正则表达式
from fake_useragent import UserAgent  # 导入伪造头部信息的模块
'''
下载批量下载视频
打印视频下载的实时进度
'''

# 哔哩哔哩小视频json地址
json_url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={page}1&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'
class Crawl():
    def get_json(self,json_url):
        headers = {'User-Agent': UserAgent().random}  # 创建随机生成的头部信息
        response = requests.get(json_url, headers=headers)  # 设置随机生成的头部信息
        # 判断请求是否成功
        if response.status_code == 200:
            return response.json()  # 返回json信息
        else:
            print('获取json信息的请求没有成功！')
    #下载视频
    def download_video(self,video_url,titlename):
        size = 0     # 记录叠加每次写入大小的变量
        headers = {'User-Agent':UserAgent().random}  #创建随机生成的头部信息
        # 下载视频的网络请求
        response = requests.get(video_url, headers=headers, stream=True)
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 视频内容的总大小
        if not os.path.exists('video'):  # 如果video目录不存在时
            os.mkdir('video')             # 创建该目录
        if response.status_code == 200:   # 判断请求是否成功
            if os.path.exists('video'):
                print('视频文件大小：%0.2fMB' % (content_size / chunk_size / 1024))  # 换算单位，并打印文件大小
                with open('video/'+titlename+'.mp4', 'wb')as f:                     # 将视频写入指定位置
                    for data in response.iter_content(chunk_size=chunk_size):      # 循环写入，实现一段一段的写
                        f.write(data)                                                # 写入视频文件
                        f.flush()                                                    # 刷新缓存
                        size += len(data)  # 叠加每次写入的大小
                        # 打印下载进度
                        print('\r 文件下载进度:%d%%(%0.2fMB/%0.2fMB)' % (float(size / content_size * 100), (size/ chunk_size / 1024), (content_size / chunk_size / 1024)), end=" ")

        else:
            print('视频下载失败！')
if __name__ == '__main__':
    ranking = 0                                           # 排名变量
    c = Crawl()
    for page in range(0,10):
        json = c.get_json(json_url.format(page=page))  # 获取返回的json数据
        infos = json['data']['items']  # 信息集
        for info in infos:             # 遍历信息
            ranking += 1  # 叠加排名
            print('\n正在下载排名第', ranking, '的视频')
            title = info['item']['description']  # 视频标题
            # 只保留标题中英文、数字与汉字，其它符号会影响写入文件
            comp = re.compile('[^A-Z^a-z^0-9^\u4e00-\u9fa5]')
            title = comp.sub('', title)  # 将不符合条件的符号替换为空
            video_url = info['item']['video_playurl']  # 视频地址
            print(title,video_url)
            c.download_video(video_url, title)  # 下载视频,视频标题作为视频的名字
        time.sleep(random.randint(3, 6))  # 随机产生获取json请求的间隔时间

