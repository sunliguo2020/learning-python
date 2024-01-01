# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 9:12
"""
import _thread
import time

import win32api


def run():
    win32api.MessageBox(0, '人生苦短')


if __name__ == '__main__':
    for i in range(4):
        _thread.start_new_thread(run, ())
    print('over')
    time.sleep(10)
