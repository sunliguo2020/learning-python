# *_* coding : UTF-8 *_*
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import requests  # 导入网络请求模块
import re        # 导入正则表达式模块

def get_movies(url):
    # 头部信息
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    response = requests.get(url,headers=headers)  # 发送网络请求
    response.encoding='gb2312'                    # 设置编码方式
    if response.status_code==200:                 # 判断请求是否成功
        # 获取每个电影详情页地址,通过表达式提取电影详情页地址
        movies_info = re.findall('<a href="(.*?)" class="ulink">',response.text)
        for url in movies_info:          # 循环每个电影的详情页地址
            info_url = 'http://www.ygdy8.net'+url     # 拼接完整地址
            # 对电影详情页发送网络请求
            movies_info_response = requests.get(info_url,headers=headers)
            movies_info_response.encoding = 'gb2312'  # 设置编码方式
            # 通过表达式匹配电影的下载地址
            download_url = re.findall('<a href=".*?">(.*?)</a></td>', movies_info_response.text)
            print(download_url)     # 打印电影的下载地址
if __name__ == '__main__':
    get_movies('http://www.ygdy8.net/html/gndy/dyzz/index.html')
