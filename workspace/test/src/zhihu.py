'''
Created on 2016-4-17

@author: Administrator
'''
import httplib
import urllib2

def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


response = urllib2.urlopen('http://blog.sunliguo.com')
print type(response)
print response.read()