# *_* coding : UTF-8 *_*
# 文件名称   ：timing.py
# 开发工具   ：PyCharm

import datetime  # 导入日期时间模块
import time  # 导入时间模块
import requests  # 导入网络请求模块
from bs4 import BeautifulSoup  # 导入解析HTML代码的模块


def implement():
    # 头部信息
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    response = requests.get('http://www.waduanzi.com/', headers=headers)
    response.encoding = 'utf-8'  # 设置编码方式
    html = BeautifulSoup(response.text, "html.parser")  # 解析html代码
    info_all = html.find_all('div', class_='item-detail')  # 获取所有段子信息
    index = 1  # 文字换行标记
    for i in info_all:  # 遍历段子信息
        print('\n《', i.h2.a.text, '》\n')  # 标题内容
        # 获取段子文字信息，并标记20字左右换行包括符号
        for text in i.find('div', class_='item-content').text:
            index += 1  # 递增文字换行标记
            if index == 20:  # 达到标记要求
                print(text, '\n')  # 执行换行
                index = 0  # 初始化文字换行标记
            else:
                print(text, end='')  # 去除默认的换行
        print('\n')


def timing(hour, minute):
    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            implement()  # 启动执行的程序
            break       # 程序执行完成后自动跳出循环结束任务
        time.sleep(60)  # 每1分钟检测一次


if __name__ == '__main__':
    timing(10,34)   # 设置启动时间，时间为24小时制，例如夜间为22:00