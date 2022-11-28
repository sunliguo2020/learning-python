# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/11/28 11:22
"""
users = {'aeinstein': {'first': 'albert',
                       'last': 'eistein',
                       'location': 'princeton'},
         'mcuie': {'first': 'marie',
                   'last': 'curie',
                   'location': 'paris'}
         }
for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location  = user_info['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tlocation:{location.title()}")
