# *_* coding : UTF-8 *_*
# 文件名称   ：initData.py
# 开发工具   ：PyCharm
import requests  # 导入网络请求模块
import re        # 正则表达式模块
import json      # json模块

# 头部信息
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/72.0.3626.121 Safari/537.36'}
# 发送网络请求
response = requests.get('https://view.inews.qq.com/q/WXN20190429000048061',
                        headers=headers)
response.encoding='utf-8'  # 设置编码方式
if response.status_code==200:    # 判断请求是否成功
    # 通过正则表达式匹配initData中的json信息
    text = re.findall('<script>window.__initData = (.*?);</script>',response.text)[0]
    json_dict = json.loads(text)   # 通过json模块解析信息，同时将Unicode码转换为中文
    print(json_dict)               # 打印网页中文字的json信息