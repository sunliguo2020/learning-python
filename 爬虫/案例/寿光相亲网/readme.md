问题：
复制请求后，发现提示：
```javascript
{'code': 500, 'data': '服务错误3'}
```

请求头中字段：'hashtoken'，起作用！

搜索关键字找到：
```javascript
 s.interceptors.request.use(function(e) {
            var t = new a.a.prototype.$jsEncrypt;
            return t.setPublicKey(a.a.prototype.PublicKey),
            Object(o.getFansidKey)() && (e.headers.fansid = "bearer " + Object(o.getFansidKey)()),
            e.headers.hashtoken = t.encrypt((new Date).getTime().toString()),
            e.headers.Authorization = "Basic d2ViQXBwOndlYkFwcA==",
            e
        }
```

```javascript
i.interceptors.request.use(function(e) {
            Object(o.getFansidKey)() && (e.headers.fansid = "bearer " + Object(o.getFansidKey)()),
            Object(o.getUidKey)() && (e.headers.uid = "bearer " + Object(o.getUidKey)());
            var t = new a.a.prototype.$jsEncrypt;
            return t.setPublicKey(a.a.prototype.PublicKey),
            e.headers.hashtoken = t.encrypt((new Date).getTime().toString()),
            e
        }
```
在上面2处加断点，等待一段时间后，刷新，在第二处断住。
