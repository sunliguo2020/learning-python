#!/usr/bin/env person
#coding:utf-8
import urllib2
import re

class qiubai(object):
	def __init__(self,page=1):
		self.page = page
	def search(self,page):
		url= "http://www.qiushibaike.com/hot/page/%s" %page
		print "url =",url
		#re_qd =re.compile(r'detail.*?<a.*?>(.*?)<.*?title="(.*?)">\s*(.*?)\s*?<',re.DOTALL)
		re_qd = re.compile(r'<div class="content">(*)</div>',re.DOTALL)
		headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}  
		req = urllib2.Request(url = url,headers = headers)
		html = urllib2.urlopen(req).read()
		print html
		my_qiubai =re_qd.findall(html)
		for i in range(0,19):
			for k in range(3):
				print my_qiubai[i][k]
			s= raw_input("回车继续")
			if s == "q":
				exit()
			else:
				page = int(page)+1
				print "-"*18+"第"+str(page)+"页"+"-"*18
				self.search(page)
			print "-"*40
	def query(self):
		global p
		p = raw_input("输入要看的页数:")
		if p == "q":
			exit()
		elif not p.isdigit() or p == 0:
			print "p=0"
			self.search(p)
		else:
			print "-"*18+"第"+p+"页"+"-"*18
			self.search(p)

if __name__ == "__main__":
	print "-"*40
	print "糗百命令行版:"
	print "输入q退出程序"
	print "-"*40
	qb = qiubai()
	qb.query()