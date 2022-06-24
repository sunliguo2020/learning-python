#coding:utf-8
import urllib2
import re
from wordpress_xmlrpc import Client,WordPressPost
from wordpress_xmlrpc.method.posts import GetRecentPosts,NewPost
#连接wordpress，xmlrpc连接，后台账号，密码
wp = Client("http://xx/xmlrpc.php","","")
post = WordPressPost()

#得到html源码
def gethtml(url):
	html = urllib2.urlopen(url).read()
	return html
#得到目标URL源码
code = gethml('http://www.qingdi.com/files/article/html/4/4496/index.html')
#提取小说url以及标题
novel = re.findall(r'<a href="(\d+).html">(.+?)</a>',code)
#追加的方式记录采集到的URL
f = open(".txt","a+")
#读取txt中的url
urls = f.read()
for i in novel:
	bookurl = "http://www.qingdi.com/files/article/html/4/4496/"+i[0]+".html"
	#判断url是否在txt中
	if bookurl not in urls:
		#重要如果不在追加新的url
		open(".txt","a+").write(bookurl+"\n")
		#提取title和content
		title = i[1].decode('GBK',"ignore")
		content = re.findall(r'<div id="content">([\s\S]*?)</div>',gethtml(bookurl))[0].decode('gbk','ignore')
		post.title = title
		post.decritpion = content
		#发送到wordpress
		wp.call(NewPost(post,True))
		print "posts updates"
	else:
		print "No posts updates"
f.close()