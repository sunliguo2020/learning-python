#!/usr/bin/env python

class Bird(object):
	have_feather = True
	way_ofreproduction = 'egg'

class happyBird(Bird):
    def __int__(self,more_words):
		print "We are happy birds.",more_words


#summer = happyBird('Happy,Happy')

class Human (object):
    	def __int__(self,input_gender):
	    self.gender = input_gender
	def printGender(self):
	    print self.gender

li_lei = Human('male')
print li_lei.gender
li_lei.printGender()
