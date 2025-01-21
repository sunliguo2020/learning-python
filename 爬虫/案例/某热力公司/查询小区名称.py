# -*- coding: utf-8 -*-
"""
 @Time : 2024/11/7 21:49
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

headers = {
    "Accept": "application/json",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Pragma": "no-cache",
    "Referer": "http://www.sgjinhuireli.cn/sgwx/wechat/yhbm.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
cookies = {
    "JSESSIONID": "C494BDFAC1D7C8FC18FF8D4A1F903CDF.tomcat1",
    "49BAC005-7D5B-4231-8CEA-16939BEACD67": "admin",
    "admin": "123456"
}
url = "http://www.sgjinhuireli.cn/sgwx/wt_getXq"
params = {
    "yhmc": "",
    "fh": ""
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)

# print(response.text)
# print(response)
result = response.json()
xiaoqu_list = result.get('list')
print(xiaoqu_list)

with open('xiao.csv', 'w', encoding='utf-8', newline='\n') as fp:
    for i in xiaoqu_list:
        fp.write(i+'\n')
