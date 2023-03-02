# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-09 13:45
"""
def power(exp):
    def exp_of(base):
        return base **exp
    return exp_of

square = power(2)
cube = power(3)

print(square(4))
print(cube(4))