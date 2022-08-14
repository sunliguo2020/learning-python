# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/9/10 20:19
"""
#python excel

import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
cell = sheet['a1']
cell.value = '中国美丽'
wb.save('我的excel文件.xlsx')