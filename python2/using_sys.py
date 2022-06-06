#!/usr/bin/python

import sys

print "the commad line arguments are:"

for i in sys.argv :
    print i
print'\n\nThe pythonpath is ' , sys.path, '\n'


print sys.__name__
