# *_* coding : UTF-8 *_*

# 文件名称   ：demo02.py
# 开发工具   ：PyCharm

data = [10, 20, 30, 40, 50, 60, 70, 80]
strnull = ''
stradd = ''
strlin = ''
for item in data:
    strnull = strnull + str(item)  # 连接列表中的元素，间隔符为空
    stradd = stradd + '+' + str(item)  # 连接列表中的元素，间隔符为‘+’
    strlin = strlin + '<' + str(item)  # 连接列表中的元素，间隔符为‘<’
    if item ==80:
        print(item)
    else:
        print(item, end='*')  # 在输出设置间隔符为‘*’，连接各个元素
print(strnull)
print(stradd.lstrip('+'))
print(strlin.lstrip('<'))
