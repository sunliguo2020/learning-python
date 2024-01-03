# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-03 19:34
"""
import base64
import hashlib
import time
from Crypto.Cipher import AES
import execjs
import requests

# 时间戳
ti = str(int(time.time() * 1000))
print(ti)

js = execjs.compile(open('./you.js', 'r', encoding='utf-8').read())
# print(js)
result = js.call('fn', ti)
# print(result)

cookies = {
    'OUTFOX_SEARCH_USER_ID': '2065236079@10.55.164.99',
    'OUTFOX_SEARCH_USER_ID_NCOO': '732367065.627716',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID=2065236079@10.55.164.99; OUTFOX_SEARCH_USER_ID_NCOO=732367065.627716',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'i': '我是谁',
    'from': 'auto',
    'to': '',
    'domain': '0',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': result,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': str(ti),
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}

response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)
print(response.text)
def result(text_AES):
    #   偏移量
    decodeiv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
    # 秘钥
    decodekey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
    # 先把密匙和偏移量进行md5加密 digest()是返回二进制的值
    key = hashlib.md5(decodekey.encode(encoding='utf-8')).digest()
    iv = hashlib.md5(decodeiv.encode(encoding='utf-8')).digest()
    # AES解密 CBC模式解密
    aes_en = AES.new(key, AES.MODE_CBC, iv)
    # 将已经加密的数据放进该方法
    data_new = base64.urlsafe_b64decode(text_AES)
    # 参数准备完毕后，进行解密
    result = aes_en.decrypt(data_new).decode('utf-8')
    return result

print(result(response.text))
