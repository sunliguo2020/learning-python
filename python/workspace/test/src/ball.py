#coding:utf-8
class Ball(object):
	def __init__(self,name="sunliguo"):
		self.name = name
	def kick(self):
		print "我叫%s" % self.name

a = Ball()

a.kick()
a.__init__()

class Person:
	__name = "小甲鱼"
	def getName(self):
		return self.__name

p =Person()
print p.getName()

print p._Person__name