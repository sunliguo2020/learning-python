'''
Created on 2016-4-29

@author: Administrator
'''
import os
import time

folder = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())

print folder
print os.getcwd()


#os.makedirs(r'%s/%s'%(os.getcwd(),folder))