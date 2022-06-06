#!/usr/bin/python

def func():
	global x
	print "x is ",x
	x=2
	print "change local x to ",x
x=50
func()
print "value of x is ",x
