# -*- coding: utf-8 -*-
'''
Created on 2016-8-2

@author: sunliguo
'''
def try_to_change(n):
    n = "Mr.Gumby"
    
name = "Mrs.Entity"

try_to_change(name)

print name

def change(n):
    n[0] = "Mr.Gumby"
    
names = ["Mr.Entity","Mrs.Thing"]

change(names[:])

print names