# -*- coding: utf-8 -*-
"""
 @Time : 2024/12/10 21:00
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
下载m3u8文件
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# m3u8页面
page_url = 'http://49.233.211.165/article_comment/?id=1'

# 发送HTTP请求获取页面内容
response = requests.get(page_url)
response.raise_for_status()  # 如果请求失败，抛出HTTPError异常

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有的<a>标签，且href属性以.m3u8结尾
a_tags = soup.find_all('a', href=lambda href: href and href.endswith('.m3u8'))

# 遍历每个<a>标签
for a_tag in a_tags:
    # 提取href属性
    href = a_tag['href']

    # 解析完整的URL（如果href是相对路径）
    full_url = urljoin(page_url, href)
    # 正则表达式模式
    # 播放m3u8页面，只提取后面的url
    pattern1 = re.compile(r"/play_m3u8/\?url=(.+)")
    pattern2 = re.compile(r"/(.+)\.m3u8")

    match1 = pattern1.match(href)
    if match1:
        # 第一种类型：提取 ?url= 后面的部分
        url = match1.group(1)
        full_url = url

    # 使用链接文本（去除前后空白字符）作为目录名
    directory_name = a_tag.get_text(strip=True)

    # 替换或删除目录名中的非法字符（可选）
    # 例如，将空格替换为下划线，或删除特殊字符
    directory_name = directory_name.replace(' ', '_').replace('/', '_') # 示例替换
    # 或者使用更严格的清理方法
    # import re
    # directory_name = re.sub(r'[^a-zA-Z0-9_]', '_', directory_name)  # 只保留字母、数字和下划线

    # 确保目录存在
    os.makedirs(directory_name, exist_ok=True)

    # 下载.m3u8文件
    response = requests.get(full_url, stream=True)
    response.raise_for_status()

    # 获取文件名（从URL的路径部分）
    # parsed_url = urlparse(full_url)
    file_name = os.path.basename(full_url)

    # 将文件写入到指定路径
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f'Downloaded {file_path}')

print('All done!')
