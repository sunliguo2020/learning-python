```python

class BookView2(APIView):
    def post(self,request):
        print(type(request.data))
        print(request.data)
        return HttpResponse(f"request.data{request.data}")
```



1、post body为空

```
POST /app1/book2/ HTTP/1.1
User-Agent: PostmanRuntime/7.32.3
Accept: */*
Postman-Token: dc9a28a1-0327-4164-a748-a5fbe4ef8efa
Host: 127.0.0.1:8000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0

HTTP/1.1 200 OK
Date: Tue, 18 Jul 2023 10:59:38 GMT
Server: WSGIServer/0.2 CPython/3.10.5
Content-Type: text/html; charset=utf-8
Vary: Accept, Cookie
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 14
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

request.data{}
```

2、post body 为form-data

```python
POST /app1/book2/ HTTP/1.1
User-Agent: PostmanRuntime/7.32.3
Accept: */*
Postman-Token: f846e324-bdb6-41f2-8775-3fff25a09ae6
Host: 127.0.0.1:8000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: multipart/form-data; boundary=--------------------------150014595292496679396416
Content-Length: 258

----------------------------150014595292496679396416
Content-Disposition: form-data; name="a"

1
----------------------------150014595292496679396416
Content-Disposition: form-data; name="b"

2
----------------------------150014595292496679396416--
HTTP/1.1 200 OK
Date: Tue, 18 Jul 2023 11:02:20 GMT
Server: WSGIServer/0.2 CPython/3.10.5
Content-Type: text/html; charset=utf-8
Vary: Accept, Cookie
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 49
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

request.data<QueryDict: {'a': ['1'], 'b': ['2']}>
```

3、body为 x-www-form-urlencoded

```python
POST /app1/book2/ HTTP/1.1
User-Agent: PostmanRuntime/7.32.3
Accept: */*
Postman-Token: 8d81d2b5-f419-4344-81bf-a0f01d26a527
Host: 127.0.0.1:8000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 7

a=1&b=2HTTP/1.1 200 OK
Date: Tue, 18 Jul 2023 11:03:39 GMT
Server: WSGIServer/0.2 CPython/3.10.5
Content-Type: text/html; charset=utf-8
Vary: Accept, Cookie
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 49
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

request.data<QueryDict: {'a': ['1'], 'b': ['2']}>
```

4、body 为json

```python
POST /app1/book2/ HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.32.3
Accept: */*
Postman-Token: e17e5b2e-4b3a-4666-b32e-ef726bd1c752
Host: 127.0.0.1:8000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 13

{"a":1,"b":2}HTTP/1.1 200 OK
Date: Tue, 18 Jul 2023 11:05:11 GMT
Server: WSGIServer/0.2 CPython/3.10.5
Content-Type: text/html; charset=utf-8
Vary: Accept, Cookie
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 28
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

request.data{'a': 1, 'b': 2}
```

