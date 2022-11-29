#!/usr/bin/python

number=12

guess = int(raw_input('Enter an integer:'))

if guess == number : 
	print "You guess"
elif guess < number:
    	print "lower"
else:  
    	print "hinger"
print "Down" 
