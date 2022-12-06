Django 和Flash获取访问来源referer

### Flask

```python
request.referer #来路
request.headers.get('User-Agent') #请求头

```

#### Django

```python
request.META['HTTP_REFERER']	#来路
request.META['HTTP_USER_AGENT'] #请求头
```

