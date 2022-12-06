

HTTP请求包含：请求行、请求头、消息主题数据

```python
<method> <url> <version>
<headers>
<entity-body>
```



```python
POST /depart/add/ HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 118
Content-Type: application/x-www-form-urlencoded
Cookie: csrftoken=dl9GSKXeVMw4CgrTsKoHBn7M2TzOQDIe; sessionid=1yv8l67gyk9s188ihgjoens7njhs9cg9
Host: 127.0.0.1:8000
Origin: http://127.0.0.1:8000
Pragma: no-cache
Referer: http://127.0.0.1:8000/depart/add/
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62
sec-ch-ua: "Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
```

其中Content-Type告诉服务端，用什么方式解析消息主题。同时发送数据的客户端也对数据采用同样的编码方式。

post方法中有四种编码方式，默认的是application/x-www-form-urlencoded，最方便的是application/json。

四种方式包括：

``` python
application/x-www-form-urlencoded (URL encoded)
multipart/form-data (键值对型数据)
application/json (json类型数据)
text/xml （xml)
```

### Requests表示这四种方式：

```python
data = {
    "name":'xxxx'
}
```

1、application/x-www-from-urlencoded

data = 传入参数

```python
requests.post(url='http://httpbin.org/post',data=data,headers={"Content-type":"application/x-www-form-urlencoded"}).json()
```

2、multipart/form-data

data = 传参 数据的编码方式不同

```python
from requests_toolbelt import MultipartEncoder

m = MultipartEncoder(
    fields={'field0': 'value1', 'field1': 'value2', 'field2': ('filename', open('data.txt', 'rb'), 'text/plain')}
    )
requests.post(url="http://httpbin.org/post",data=m, headers={"Content-type": "multipart/form-data"}).json()
```

3、application/json

json = 传入参数

```python
import json
p_data = json.dumps(p_data)
requests.post(url="http://httpbin.org/post",json=p_data, headers={"Content-type": "application/json"}).json()
```

