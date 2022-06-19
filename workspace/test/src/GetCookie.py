#_*_coding:utf-8_*_
'''
Created on 2016-4-29

@author: Administrator
'''

import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()

#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)


#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

#print response.read()
#f = urllib2.urlopen(url) with open("code2.zip", "wb") as code:   code.write(f.read()) 


open("a.txt",'wb').write(response.read())