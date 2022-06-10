
def func1 (num):
	def func2(num1):
		return num+num1
	return func2
	
func = func1(10)

res = func(20) 
print res	