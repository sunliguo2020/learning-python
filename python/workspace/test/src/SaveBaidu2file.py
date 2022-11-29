'''
Created on 2016-4-29

@author: Administrator
'''

import urllib2

url = "http://www.baidu.com"

response = urllib2.urlopen(url)

file = "D:/a.html"

open(file,"wb").write(response.read())