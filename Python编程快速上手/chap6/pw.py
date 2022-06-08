# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/29 16:18
"""

# py.py  - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmAlvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] -copy account password')
    sys.exit()
account = sys.argv[1]  # first command line arg is the account name
