# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/15 22:05
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 6.代码实现.py
 @Project : learning-python
"""
import requests
import ddddocr
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import execjs

# 获取cookie
url = 'https://xuexi.chinabett.com/'
res = requests.get(url)

cookie_dict = res.cookies.get_dict()
print(f"cookie 1:{cookie_dict}")
content = res.content

# 保存网页
with open('login.html', 'wb') as fp:
    fp.write(res.content)

# 找到验证码url
soup = BeautifulSoup(content, 'lxml')
# print(soup.title)
# 直接获取，url后面不带时间戳
code_img = soup.find(id='imgVerifity')
# print(code_img)
code_url = urljoin(url, code_img.get('src'))
# print(code_url)

# {"ResultType":3,"Success":false,"Message":"验证码输入错误！","LogMessage":null,"AppendData":null}

# 图片识别
code_res = requests.get(code_url, cookies=cookie_dict)
ocr = ddddocr.DdddOcr(show_ad=False)

# cookie_dict = cookie_dict.update(code_res.cookies)
cookie_dict.update(code_res.cookies)

print(f"cookie 2:{cookie_dict}")
# 保存截图
with open('code.jpg', 'wb') as fp:
    fp.write(code_res.content)

code = ocr.classification(code_res.content)
print(code)

# 准备登录
login_url = 'https://xuexi.chinabett.com/Login/Entry'

userAccount = 'wupeiqi'
password = '112233'
with open('v3.js', 'r', encoding='utf-8') as fp:
    js_content = fp.read()
JS = execjs.compile(js_content)

userAccount = JS.call('base64encode', userAccount)
print(userAccount)
password = JS.call('base64encode', password)
password = JS.call('encryptPwd', password)
# {"ResultType":7,"Success":false,"Message":"Base-64 字符数组或字符串的长度无效。","LogMessage":null,"AppendData":null}

print(password)

login_data = {
    "userAccount": userAccount,
    "password": password,
    "returnUrl": "/PersonalCenter",
    "proVing": code
}

login_res = requests.post(login_url, data=login_data, cookies=cookie_dict)
print(login_res.text)
