from pyecharts.charts import WordCloud
from jieba import analyse

# 基于TextRank算法从文本中提取关键词
textrank = analyse.textrank
text = open('111.txt','r',encoding='gbk').read()
keywords = textrank(text,topK=30)
list1=[]
tup1=()
# 输出提取的关键词
for keyword, weight in textrank(text,topK=30, withWeight=True):
    print('%s %s' % (keyword, weight))
    tup1=(keyword,weight)  #关键词权重
    list1.append(tup1)     #添加到列表中
    
mywordcloud=WordCloud()
mywordcloud.add('',list1,word_size_range=[20,100])
mywordcloud.render('wordclound.html')
