# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2025/4/8 18:04
"""
from login import login
BASE_HOST = '192.168.1.21'

if __name__ == '__main__':
    # http://127.0.0.1:8000/get/daglperson/1783233/
    session = login(f'http://{BASE_HOST}/account/login/')
    for i in range(230062, 1000000):
        url = f'http://{BASE_HOST}/get/daglperson/{i}/'
        print(url)
        session.get(url)
