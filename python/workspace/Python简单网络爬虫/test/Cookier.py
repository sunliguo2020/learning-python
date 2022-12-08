#-*- coding:utf-8-*-

'''
Created on 2016-4-18

@author: Administrator
'''
import urllib2,cookielib

#创建cookie容器

cj = cookielib.CookieJar()

print 'type(cj):' , cj

#创建一个opener

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

print 'type(opener)',type(opener)

#给urllib2安装openrer

urllib2.install_opener(opener)

#使用带有cookie的urllib2访问网页

response = urllib2.urlopen("http://www.sunliguo.com")

print response.read()

