#coding:utf-8
'''
person 局部变量与全局变量
'''

language = "pythopersondef foo1():
	language="hello"
	print language 
def foo2():
	print language 
def foo3():
	global language 
	language = "hello" 
	print language 
foo1()
foo2()
foo3()

print language