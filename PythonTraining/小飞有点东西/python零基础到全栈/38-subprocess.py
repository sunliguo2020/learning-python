# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-30 9:58
"""
import subprocess

obj = subprocess.Popen('tree', shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       )
res = obj.stdout.read()
print(res.decode('gbk'))
res = obj.stderr.read()
print(res.decode('gbk'))