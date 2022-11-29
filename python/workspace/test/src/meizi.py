#!/usr/bin/person
#coding:utf-8
import json
import urllib2
import urllib

url = "http://www.tngou.net/tnfs/api/list"
url1="http://www.tngou.net/tnfs/api/list?page=4&rows=200"
pargm = {'page':4,"row":200}

#r = request.get(url,pargm).json()
#request = urllib2.Request(url,urllib.urlencode(pargm))

r=urllib2.urlopen(url1).read()
j=json.loads(r) 
print j

def saveImage(imgUrl,imgName):
    #response = request.get(imgUrl,stream = True)
    response = urllib2.urlopen(imgUrl)
    image = response.read()
    dst = './img/'
    path = dst+imgName
    print "save the file :"+path
    with open(path,"wb") as a:
		a.write(image)
    a.close()

def run():
    for line in j['tngou']:
        #print line
        title = line['title']
        img = line['img']
        #print "title = %s ,img = %s " %(title,img)
        src_path = "http://tnfs.tngou.net/image" +img
        saveImage(src_path,title+'.jpg')
        #print src_path
run()