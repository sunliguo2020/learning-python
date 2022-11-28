#!/usr/bin/person
# -*- coding: utf-8 -*-
'''
Created on 2016-7-17

@author: 
'''
import os
import shutil


file =open("outfile","w+")

filelist = os.walk("./").next()[2]
file.write(repr(filelist).replace("', '",'\n').replace("['","").replace("']",""))
file.seek(0)
Total=len(file.readlines())

print "Total = ",Total

file_1215=0
file_zero=0
file_428=0

if not os.path.isdir('./1215'):
    os.mkdir('./1215')
if not os.path.isdir('./zero'):
    os.mkdir('./zero') 
if not os.path.isdir('./428'):
    os.mkdir('./428')  
	

file.seek(0)

i = file.readline()
while i:
    j = i[:-1] #if os.path.isfile(j) and j.endswith(".txt"):
    if j.endswith(".txt") :
		fileSize = os.path.getsize(i[:-1])
		print "Total:%r :file %s 's size is %r"  % (Total,i[:-1],fileSize)
		if  fileSize > 1201:
			shutil.move(j,'./1215/')
			file_1215+=1
		elif fileSize == 0:
			shutil.move(j,'./zero/')
			file_zero+=1
		elif fileSize == 428:
			shutil.move(j,'./428/')
			file_428+=1
    Total=Total-1	
    i = file.readline()
	
print "file_1215  = %r file_zero = %r file_428 = %r" %(file_1215,file_zero,file_428)
file.close()