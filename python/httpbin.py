import urllib.parse,urllib.request

url = "http://httpbin.org/post"

data={'name':'sunliguo'}
data=bytes(urllib.parse.urlencode(data),encoding='utf-8')

response = urllib.request.urlopen(url,data)
print(response.read())