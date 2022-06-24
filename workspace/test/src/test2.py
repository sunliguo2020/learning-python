'''
Created on 2016-4-17

@author: Administrator
'''
age = 11

if age >= 18:
    print 'your age is ' ,age
    print 'adult'
sum = ''
names = ['Michael', 'Bob', 'Tracy',('a',age),['d','bsdfa']]
for name in names:
    if isinstance(name,(list,tuple)) :
        for i in name:
            sum +=  str(i)
    else:            
        sum +=  str(name)
print sum