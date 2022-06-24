#_*_coding:utf-8_*_
'''
Created on 2016-4-29

@author: Administrator
'''

import urllib,urllib2,cookielib

filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True,ignore_expires=True)