# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/15 21:09
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import re
import subprocess

def exec_value(hex_string):
    res = subprocess.check_output(f"node xxx.js {hex_string}")
    char_string = res.decode('utf-8').strip()

    return char_string

value = exec_value('0x495')
print(value)


