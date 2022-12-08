'''
Created on 2016-4-17

@author: Administrator
'''
import os

def cal(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

def fact(n):
    if n==1:
        return 1
    return n*fact(n - 1)


L = []
n = 1

while n <=99:
    L.append(n)
    n=n+2
    
print L


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
 
 
print len(L)

print L[:2]


for d in os.listdir('.'):
    print d