#coding:utf-8

import urllib2,urllib,re

def getpage(url):
    #url = "http://www.qiushibaike.com"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.3'}
    request = urllib2.Request(url,headers=headers)

    html = urllib2.urlopen(request)
    return html.read().decode('utf-8')

def getItem(url):
    html = getpage(url)
    pattern = re.compile(r'<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>',re.S)
    items = re.findall(pattern,html)
    for i,k in  items:
		print k
if __name__ == "__main__":
    
    for i in range(1,1000):
        #print i
        url = "http://www.qiushibaike.com/8hr/page/"
        url =  url+ str(i)
        getItem(url)