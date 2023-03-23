# *_* coding : UTF-8 *_*
# 文件名称   ：to_excel_cover.py
# 开发工具   ：PyCharm

import pandas  # 导入pandas模块
from openpyxl import load_workbook  # 导入excel操作模块

df = pandas.read_excel('demo.xlsx')  # 读取excel文件
book = load_workbook('demo.xlsx')  # 加载文件
# 创建写入对象
writer = pandas.ExcelWriter('demo.xlsx', engine='openpyxl')
writer.book = book
# 获取所有sheet
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
df['Add'] = [10, 20, 30, 40, 50]  # 添加Add列数据
# 写入数据
df.to_excel(writer, "Sheet1", index=0, startrow=0, startcol=0)
writer.save()  # 保存
