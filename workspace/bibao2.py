#coding:utf-8
def func1():
	mylist = [0]
	#外部函数
	def func2():
		mylist[0] += 1
		return mylist[0]
	return func2


func = func1()
res1 = func()
print res1
res2 = func()
print res2
res3 = func()
print res3
res4 = func()
print res4
res5 = func()
print res5