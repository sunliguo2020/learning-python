# *_* coding : UTF-8 *_*

# 文件名称   ：demo01.py
# 开发工具   ：PyCharm

name='王李张李陈王杨张吴周王刘赵黄吴杨'
newname=''
for char in name:
    if char not in newname:
        newname+=char
print (newname)
