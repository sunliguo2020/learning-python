# -*- coding: utf-8 -*-
'''
 @Time : 2022/6/12 6:30
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : pizza.py
 @Project : learning-python
'''


def make_pizza(*toppings):
    '''
    打印顾客点的所有配料。
    '''
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
