# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-27 15:01
"""


def add_list(in_func_obj):
    print(f"In add [before]: in_func_obj='{in_func_obj}'")
    in_func_obj += ['baz']
    print(f"In add [after]: in_func_obj='{in_func_obj}'")


orig_obj = ['foo', 'bar']
print(f'Outside [before]:orig_obj = "{orig_obj}"')
add_list(orig_obj)
print(f'Outside [after]:orig_obj = "{orig_obj}"')
