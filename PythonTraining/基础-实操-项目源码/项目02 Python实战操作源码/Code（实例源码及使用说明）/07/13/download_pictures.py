# *_* coding : UTF-8 *_*
# 文件名称   ：download_pictures.py
# 开发工具   ：PyCharm

import urllib.request   # 导入urllib.request模块
# from urllib.request import urlretrieve  # 直接远程下载图片
import requests  # 导入网络请求模块
import os          # os模块
import shutil      # 文件夹控制
def download_pictures(url):
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    response = requests.get(url,headers=headers)  # 发送网络请求，获取服务器响应
    json_str = str(response.json())  # 将请求结果的json信息转换为字符串
    dict_json = eval(json_str)  # 将json字符串信息转换为字典，方便提取信息
    # 每次获取数据之前，先将保存图片的文件夹清空，清空后再创建目录
    if os.path.exists('img_download'):  # 判断img目录是否存在
        shutil.rmtree('img_download')  # 删除img目录
        os.makedirs('img_download')  # 创建img目录
    else:
        os.makedirs('img_download')  # 创建img目录
    for index, i in enumerate(dict_json['products']):
        if index <= 10:
            # 图片地址
            imgPath = 'http://img13.360buyimg.com/n1/s320x320_' + i['imgPath']
            urllib.request.urlretrieve(imgPath, 'img_download/' + 'img'+str(index) + '.jpg')  # 根据下标命名图片名称
if __name__ == '__main__':
    download_pictures('https://ch.jd.com/hotsale2?cateid=686')