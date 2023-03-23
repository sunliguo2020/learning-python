# *_* coding : UTF-8 *_*

# 文件名称   ：demo03.py
# 开发工具   ：PyCharm
name = '王李张李陈王杨张吴周王刘赵黄吴杨'
myname = set(name)
print(myname)
newname = list(set(name))
print(''.join(newname))
newname.sort(key=name.index)
print(newname)
print(''.join(newname))
