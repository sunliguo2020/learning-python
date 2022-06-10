import requests
import random
import string

total_string = string.digits + "abcdef"

session = requests.Session()

# 1.获取buvid3
session.get(
    url="https://www.bilibili.com/video/BV1xL4y1E78r",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
)
res = session.get(
    url="https://api.bilibili.com/x/frontend/finger/fpfmc",
    params={
        # "fp": "c477f68778b883555657f289950f4f0a" # 32字符串
        "fp": "".join([random.choice(total_string) for i in range(32)])  # 32字符串
    }
)

print(res.text)
