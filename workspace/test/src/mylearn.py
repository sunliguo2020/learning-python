#!/usr/bin/evn person

class Firstclass:
	a = 78
	def setdata(self,value):
		self.data = value
		a = value
	def display(self):
		print self.data


Firstclass().setdata(1)

x=Firstclass()
y=Firstclass()

print x.a
print y.a

x.setdata("aa")
x.display()

print x.a

''''
class Mylearn():
	b = "def"
	def test1(self):
		self.a = "abc"
		#print self.a
	def test2(self):
		print self.a

example= Mylearn()

#example.test1()
print example.b
#print id(example.test2())

# print id(example.a)
# for i in  dir(example):
# 	print i,dir(i)
'''