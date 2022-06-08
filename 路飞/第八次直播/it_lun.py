# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/4 19:58
"""
from urllib import request
import requests
import re
main_url = 'http://md.itlun.cn/a/nhtp/'
response = requests.get(url=main_url)
#处理页面中的中文乱码
response.encoding = 'gbk'
#获取了页面源码数据
page_text = response.text

#数据解析：解析图片的地址
# ex = '<li>.*?<img.*?src="(.*?)" style.*?</li>'
#re.S用来处理回车
# img_src_list = re.findall(ex,page_text,re.S)
#注意：如果确认正则没有写错，则取关注下正则作用到的页面源码是否出现问题
#极有可能页面源码数据出现了动态加载的情况
#在抓包工具中，查看了数据包的响应数据，发现img，li标签都是大写，而我们写的正则匹配的是小写标签，因此匹配失败
# ex = '<LI>.*?<IMG.*?src="(.*?)" style.*?</LI>'
# img_src_list = re.findall(ex,page_text,re.S)
#问题：提取到的图片地址都是一样的。如何解决？继续查看抓包工具的源码
#发现：真正的图片地址是有js动态加载出来的
ex = '<script.*?src = "(.*?)"; </script>'
img_src_list = re.findall(ex,page_text,re.S)
#发现解析出的图片地址，是不完整的，缺少http:
for img_src in img_src_list:
    img_src = 'http:'+img_src
    # print(img_src)
    img_name = img_src.split('/')[-1]
    request.urlretrieve(img_src,img_name)
    print(img_name,'下载成功！')