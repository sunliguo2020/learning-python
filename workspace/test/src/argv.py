'''
Created on 2016-5-2

@author: Administrator
'''
import sys

if __name__ == "__main__":
    print len(sys.argv)
    print type(sys.argv)
    for i in sys.argv:
        print i