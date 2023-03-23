# *_* coding : UTF-8 *_*

# 文件名称   ：demo02.py
# 开发工具   ：PyCharm
name=input('姓名：')
phone=input('电话：')
university=input('学校：')
data=name,phone,university
print(data )
print(' '.join(data) )
print(name,phone,university)
