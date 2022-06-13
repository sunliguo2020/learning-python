# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/28 19:56
"""
birthdays = {'Alice': 'Apr 1',
             "Bob": 'Dec 12',
             "Carol": "Mar 4"}
print(birthdays)
while True:
    print("Enter a name :(blank for quit)")
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated")
