#!/usr/bin/person

import os
import time

Total =0 

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
fileList = os.listdir('./')
for i in fileList:
	if os.path.isdir(i):
		#dir_len = len(os.listdir(i))		
		count = 0
		for root,dirs,files in os.walk(i):
			fileLength = len(files)
			if fileLength !=0:
				count=count+fileLength
		print "%s:\t%r" %(i,count)
		
		Total = Total+count

print "Total:\t%r" % Total