# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/11/28 11:07
"""
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

print(type(user_0.items()))