# *_* coding : UTF-8 *_*

# 文件名称   ：demo01.py
# 开发工具   ：PyCharm
nba='哈登: 31.6  伦纳德: 31.2   乔治: 28.6    库里: 27.3    利拉德:26.9'
nbanew=nba.split(' ')
nbaone=[i for i in nbanew if i !='']
print(nbaone)
