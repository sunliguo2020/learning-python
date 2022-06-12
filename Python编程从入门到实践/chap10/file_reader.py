# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2021/2/10 14:30
"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(len(contents))
#print(contents,end='')
print(contents)
print('*'*20)
print(contents.rstrip())
print('*'*20)


filename = 'pi_digits.txt'
with open(filename) as file_object:
    print(type(file_object))
    print(dir(file_object))
    count = 0
    for line in file_object:
        print("count=",count)
        print(line,end='')
        count +=1