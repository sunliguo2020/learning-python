# *_* coding : UTF-8 *_*

# 文件名称   ：demo05.py
# 开发工具   ：PyCharm
name='王李张李陈王杨张吴周王刘赵黄吴杨'
zd={}.fromkeys(name)
mylist=list(zd.keys())
# mylist = list({}.fromkeys(name).keys())
print (''.join(mylist))
