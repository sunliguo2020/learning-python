# -*- coding: utf-8 -*-

"""
@author: AN

@contact: 

@Created on: 2019/11/23 14:22
"""
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)