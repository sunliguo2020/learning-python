import requests

res = requests.get(
    url="https://www.bilibili.com/video/BV1XA411779D",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
)

print(res.cookies.get_dict())
