import requests
from bs4 import BeautifulSoup

# https://www.amazon.com/gp/product/B07YN82X3B/
res = requests.get(
    url="https://www.amazon.com/gp/product/B07YN82X3B/?th=1",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "cache-control": "no-cache",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
)

# print(res.text)

soup = BeautifulSoup(res.text, 'lxml')
print(soup)
title = soup.find(id="productTitle").text.strip()
print(title)
