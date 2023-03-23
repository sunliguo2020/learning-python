import re
import matplotlib.pyplot as plt
from matplotlib import colors
import jieba
import wordcloud
from wordcloud import WordCloud
import imageio
# 读取文件
str1 = open('joker.txt','r').read()
#文本数据处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|\[|\]|  ；|，|。|"')
str1 = re.sub(pattern, '', str1)
#自定义小丑颜色
color_list=['darkslategray','red','orange','darkred']
colormap=colors.ListedColormap(color_list) 
#文本分词处理制作词云
cut_text = jieba.cut(str1, cut_all=True)     # cut_all=False 表示采用精确模式
word = ' '.join(cut_text)
#图片背景
pic = imageio.imread('小丑.png')
#设置中文停用词
stopwords = set('')
stopwords.update(['展开','回应','一个','影评','可能','一部','没有','我们','这个','这部','电影','就是'
                    ,'大家','不是','只是','因为','一些','本片'])
#生成词云图
wd = wordcloud.WordCloud(
    mask=pic,
    font_path='simhei.ttf',
    colormap=colormap,
    stopwords = stopwords,
    background_color='white'
    )
#将长文本分词并去除屏蔽词
process_word = WordCloud.process_text(wd,word)
#对文本词排序(根据字典中值的大小，对字典中的项排序)
sort = sorted(process_word.items(),key=lambda x:x[1],reverse=True)
print(sort[:50]) # 输出文本词频最高的前50个词
wd.generate(word)
plt.imshow(wd)
plt.axis('off')
plt.show()
