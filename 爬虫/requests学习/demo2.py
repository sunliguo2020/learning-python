import requests

req = requests.get('http://www.baidu.com')
print(req.headers)