# -*- coding: utf-8 -*-
"""
 @Time : 2024/11/7 21:33
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://www.sgjinhuireli.cn",
    "Pragma": "no-cache",
    "Referer": "http://www.sgjinhuireli.cn/sgwx/info/khxx.jsp",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
cookies = {
    "JSESSIONID": "C494BDFAC1D7C8FC18FF8D4A1F903CDF.tomcat1",
    "49BAC005-7D5B-4231-8CEA-16939BEACD67": "admin",
    "admin": "123456"
}
url = "http://www.sgjinhuireli.cn/sgwx/wx_getKhxx"

data = {
    "xq": "巴龙国际北区",
    "lh": "A7",
    "dyh": "1",
    "fh": "202"
}
response = requests.post(url,
                         headers=headers,
                         cookies=cookies,
                         data=data,
                         verify=False)

# print(response.text)
print(response.content)
