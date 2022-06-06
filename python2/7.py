#!/usr/bin/python 
x="a"
while x != "q":
    print "hello"
    x = raw_input("please input something:q for quit")
    if not x:
	break
