url：https://m.hltmsp.com/passport/login
```bash
curl 'https://api.hltmsp.com/user/index/login' \
  -H 'accept: */*' \
  -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'origin: https://m.hltmsp.com' \
  -H 'pragma: no-cache' \
  -H 'referer: https://m.hltmsp.com/' \
  -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'sec-ch-ua-platform: "Android"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36' \
  --data-raw 'mobile=15653613200&password=123456&platformId=1&shop_id=6&token=&ident=1a67a89e235c94d815532e74acc50be0&appid=duty_h5&nonce_str=7drgdd75cs7c6fej3t&time_stamp=97343807473&sign=55D8BFC6FDFCF4CC0B6C6F180443DFCB'
```

破解请求参数的生成：
1、nonce_str
直接搜索关键词，找到两个。两个打断点，排除一个。
```javascript
  setSignData: function(data) {
                data || (data = {}),
                data.appid = "duty_h5";
                var e = "hltmsp5615466";
                4 != data.platformId && 5 != data.platformId || (data.appid = "duty_app",
                e = "hltmsp89226416"),
                2 != data.platformId && 6 != data.platformId && 8 != data.platformId && 11 != data.platformId || (data.appid = "duty_xcx",
                e = "hltmsp5689456"),
                data.nonce_str = l.b.randomStr(Math.floor(26 * Math.random()) + 6);
                var t = 2022051288 + Math.floor(Date.now() / 1e3) + ""
                  , n = Math.floor(9 * Math.random()) + 1;
                t = "" + n + t.substring(t.length - n, t.length) + t.substring(0, t.length - n),
                data.time_stamp = t;
                var o = "";
                return Object.keys(data).sort().map((function(e) {
                    null === data[e] || void 0 === data[e] || "" === data[e] || Array.isArray(data[e]) || (o += "".concat(e, "=").concat(data[e], "&"))
                }
                )),
                o += "app_key=".concat(e),
                (data = JSON.parse(JSON.stringify(data))).sign = r()(o).toUpperCase(),
                data
            }
```

找到生成的地方：data.nonce_str = l.b.randomStr(Math.floor(26 * Math.random()) + 6);
Math.floor(26 * Math.random()) + 6 获取一个随机值
主要精力在l.b.randomStr()函数上。
```javascript
     randomStr: function(e) {
                for (var t = "abcdfsdferwrjhtjfdgofdgfdgrew1234569798ere", n = "", o = t.length, i = 0; i < e; i++)
                    n += t.charAt(Math.floor(Math.random() * o));
                return n
            }
```

找到加载器?