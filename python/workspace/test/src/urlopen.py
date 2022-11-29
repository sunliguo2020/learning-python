# -*- coding: utf-8 -*-
'''
Created on 2016-7-26

@author: sunliguo
'''
import urllib2
url = "http://www.qiushibaike.com/hot/page/1"
headers = {  
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        }  
req = urllib2.Request(  
            url = url,
            headers = headers
        )
html = urllib2.urlopen(url).read()

print html