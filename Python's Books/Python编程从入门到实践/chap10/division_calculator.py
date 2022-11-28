# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2021/2/11 21:48
"""
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")