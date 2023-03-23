# *_* coding : UTF-8 *_*

# 文件名称   ：demo01.py
# 开发工具   ：PyCharm
username = '  明日科技  '
print(username.strip())

word='赵 钱 孙 李 周 吴 郑 王'
word=''.join([i.strip(' ') for i in word])
print(word)
