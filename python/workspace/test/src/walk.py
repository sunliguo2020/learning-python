#coding:utf-8
import os
count =0
for root,dictorys,files in os.walk('./'):
	#print root
	for i in files:
		print root,i
		count += 1

print "count =" ,count
