#coding:utf-8
import random as r


class Fish(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.x = r.randint(0,10)
		self.y = r.randint(0,10)
	def move(self):
		self.x -=10
		print "我的位置在：",self.x,self.y	
class Glodfish(Fish):
	pass
class Carp(Fish):
	pass
class Salmon(Fish):
	pass
class Sark(Fish):
	def __init__(self):

		#super().__init__()
		Fish.__init__(self)
		self.hungry = True
		
	def eat(self):
		if self.hungry:
			print "吃货的梦想就是天天想吃"
			self.hungry=False
		else:
			print "太撑了----"	

s =Salmon()

s.move()
shark = Sark()
shark.move()