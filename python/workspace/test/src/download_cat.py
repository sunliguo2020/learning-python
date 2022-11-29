#coding:utf-8
import urllib2

url = "http://placekitten.com/500/600"

response = urllib2.urlopen(url)
cat = response.read()

with open("cat.jpg","w") as f:
	f.write(cat)