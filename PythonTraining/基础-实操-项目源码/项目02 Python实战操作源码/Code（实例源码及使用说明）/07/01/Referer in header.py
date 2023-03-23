# *_* coding : UTF-8 *_*
# 文件名称   ：Referer in header.py
# 开发工具   ：PyCharm

import requests   # 导入网络请求模块
import json       # 导入json模块

# 头部信息
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
         ,'Referer':'http://www.weather.com.cn/weather1d/101010100.shtml'}
url = 'http://d1.weather.com.cn/sk_2d/101010100.html?_=1555986533582'  # 网络请求地址
response = requests.get(url,headers = headers)   # 发送网络请求
if response.status_code==200:                    # 判断请求是否成功
    response.encoding='utf-8'                    # 编码返回信息
    json_str = response.text.replace('var dataSK =','')  #  将json字符串中var dataSK =去除
    json_info = json.loads(json_str)                     # 将json字符串转换为字典类型
    print('城市：',json_info['cityname'])                # 打印json中的城市
    print('当前温度：',json_info['temp'])                # 打印温度
    print('相对湿度：',json_info['SD'])                  # 打印湿度
    print('风向等级：',json_info['WD'],json_info['WS'])  # 打印风向等级
    print('空气质量pm2.5:',json_info['aqi_pm25'])        # 打印空气质量
    print('车辆限号为：',json_info['limitnumber'])       # 打印车辆限号