```python
  jd_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    resp = requests.get(url=base_url, headers=jd_headers)
    tree = etree.HTML(resp.text)
    li_list = tree.xpath('//ul[@class="gl-warp clearfix"]/li')
    for li in li_list:
        """
        <img width="220" height="220" data-img="1" data-lazy-img="//img12.360buyimg.com/n7/jfs/t1/111789/21/25219/92851/6246a22dEe36375a5/fbf44bf375a9e447.jpg" source-data-lazy-img="">
        """
        jd_phone_pic = li.xpath('.//div[@class="p-img"]/a/img/@data-lazy-img')[0]

        jd_phone_pic = urllib.parse.urljoin(base_url, jd_phone_pic)

        print(jd_phone_pic)
```

