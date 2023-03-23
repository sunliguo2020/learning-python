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
# 制作词云
cut_text = jieba.cut(str1, cut_all=True)     # cut_all=False 表示采用精确模式
word = ' '.join(cut_text)

#小丑
pic = imageio.imread('小丑.png')
#读取停止词文件并保存到列表中
stopwords = [line.strip() for line in open('stopwords.txt').readlines()]
newword=''
#滤除停用词
for s in word:
    if s not in stopwords:
         newword += s
wd = wordcloud.WordCloud(
    mask=pic,
    font_path='simhei.ttf',
    colormap=colormap,
    background_color='white'
    )
wd.generate(newword)
plt.imshow(wd)
plt.axis('off')
plt.show()


