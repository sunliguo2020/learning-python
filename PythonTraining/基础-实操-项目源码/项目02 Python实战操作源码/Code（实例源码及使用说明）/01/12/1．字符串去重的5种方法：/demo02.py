# *_* coding : UTF-8 *_*
# 文件名称   ：demo02.py
# 开发工具   ：PyCharm

name='王李张李陈王杨张吴周王刘赵黄吴杨'
newname=''
i = len(name)-1
while True:
    if i >=0:
        if name[i] not in newname:
            newname+=(name[i])
        i-=1
    else:
        break
print (newname)
