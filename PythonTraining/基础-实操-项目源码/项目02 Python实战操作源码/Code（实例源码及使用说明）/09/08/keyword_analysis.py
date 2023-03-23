from pyecharts import WordCloud
from jieba import analyse

# 基于TextRank算法从文本中提取关键词
textrank = analyse.textrank
#text = open('./data/name11.txt','r',encoding='gbk').read()
text = open('../data/111.txt','r',encoding='gbk').read()
keywords = textrank(text)
print(keywords)
list1=[]
# 输出提取的关键词
for keyword, weight in textrank(text, withWeight=True):
    print('%s %s' % (keyword, weight))
    list1.append(weight)  #关键词权重
wordcloud = WordCloud(width=800,height=500)
wordcloud.add('',keywords,list1,word_size_range=[20,100],shape='circle')
wordcloud.render('wordclound.html')
