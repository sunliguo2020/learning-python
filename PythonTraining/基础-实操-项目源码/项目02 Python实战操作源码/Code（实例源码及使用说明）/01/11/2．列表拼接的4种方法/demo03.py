# *_* coding : UTF-8 *_*
#
# 文件名称   ：demo03.py
# 开发工具   ：PyCharm

data=['上海', '广州', '上海', '成都', '上海', '上海', '北京', '上海', '广州', '北京', '上海']
strnull=data[1]+data[2]+ data[3]+data[4]                     # 连接列表中的元素，间隔符为空
stradd=data[1]+'-'+data[2]+'-'+ data[3]+'-'+data[4]   # 连接列表中的元素，间隔符为‘+’
print(strnull)
print(stradd)
