#-*- coding:utf-8 -*-
'''
Created on 2016-4-17

@author: Administrator
'''
import urllib 
import urllib2 
url = 'http://www.baidu.com' 
values = {'name' : 'Michael Foord', 
          'location' : 'pythontab', 
          'language' : 'Python' } 

data = urllib.urlencode(values) 

#req = urllib2.Request(url, data) 

#response = urllib2.urlopen(req) 

response = urllib2.urlopen(url,data)
the_page = response.read()

print the_page