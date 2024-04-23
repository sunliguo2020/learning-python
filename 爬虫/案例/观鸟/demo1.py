# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/14 19:09
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 观鸟网登录逻辑
"""
import json
import time
import base64
import io
from PIL import Image
from ddddocr import DdddOcr

import requests

site = {
    "domain": 'https://api.birdreport.cn/',
    "login": '/member/login.html'
}


def login_captcha():
    """
    获取authToken和验证码图片
    @return:
    """
    url = site.get('domain') + "member/system/auth/kaptcha?t=" + str(int(time.time() * 1000))
    print(url)
    resp: dict = requests.get(url).json()

    return resp.get('data')


def shibie(base64_str):
    """

    @param base64_str:
    @return: 识别后的验证码
    """
    # 解码base64字符串为字节数据
    decoded_bytes = base64.b64decode(base64_str)

    # 使用PIL库将字节数据转换为图片对象
    image = Image.open(io.BytesIO(decoded_bytes))
    image.save('output.png')
    # 初始化ddddocr识别器
    ocr = DdddOcr(show_ad=False)

    # 使用ddddocr进行识别
    with image as img:
        text = ocr.classification(img)

    print("识别结果:", text)

    return text


def login(account, password, token, code):
    device = {
        "os": "windows",
        "ie": False,
        "weixin": False,
        "android": False,
        "ios": False
    }
    login_url = 'https://api.birdreport.cn/member/system/auth/login'
    data = {
        "account": account,
        "authToken": token,
        "device": json.dumps(device, separators=(',', ':'), indent=None),
        "password": password,
        "user_agent": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/123.0.0.0 safari/537.36 edg/123.0.0.0",
        "vercode": code
    }
    resp = requests.post(login_url, json=data)
    print(resp.text)
    return resp.text


if __name__ == '__main__':
    result = login_captcha()
    authToken = result.get('authToken')
    image = result.get('image')
    code = shibie(image)
    login('15689266181', '123456', authToken, code)
