#!/usr/bin/python

number=23

running=True

while running:

	guess = int(raw_input('Enter an integer:'))

	if guess == number : 
		print "You guess"
		running=False
	elif guess < number:
    		print "lower"
	else:  
    		print "hinger"
else:
    print "The while loop is over"
print "Down" 
