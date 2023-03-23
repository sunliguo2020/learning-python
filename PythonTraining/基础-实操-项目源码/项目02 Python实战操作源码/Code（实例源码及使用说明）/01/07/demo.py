# *_* coding : UTF-8 *_*

# 文件名称   ：demo01.py
# 开发工具   ：PyCharm
word= input('请输入或者拷贝含有敏感词的宣传文字：\n')
sensitive= ['第一', '国家级', '最高级', '最佳', '独一无二', '一流', '仅此一次', '顶级', '顶尖', '尖端', '极品', '极佳', '绝佳', '绝对', '终极', '极致', '首个', '首选', '独家', '首发', '首次', '首款', '金牌', '名牌', '王牌', '领袖', '领先', '领导', '缔造者', '巨星', '掌门人', '至尊', '巅峰', '奢侈', '资深', '之王', '王者', '冠军']
sensitive_find=[]
newword=word
for item in sensitive:
    if word.count(item)>0:                                              # 判断敏感词出现的次数
         sensitive_find.append(item+':'+ str(word.count(item))+'次')    # 记录敏感词出现次数
         newword=newword.replace(item, '  \033[1;31m'+item+'\033[0m')   # 敏感词描红输出
print('发现敏感词如下：')
for item in sensitive_find:
     print(item)
print('敏感词位置已用星号进行标注：\n'+ newword)
