import requests

url = 'https://fanyi.baidu.com/sug'

dat = {"kw": "dog"}

# resp = requests.post(url=url, data=dat)
# print(resp.json())

resp = requests.get(url=url, params=dat)
print(resp.request.headers)

resp.close()