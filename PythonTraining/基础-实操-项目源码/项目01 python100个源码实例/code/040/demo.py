#导入matplotlib模块pyplot函数并使用as给函数起个别名plt
import matplotlib.pyplot as plt    
import jieba                       #导入jieba分词模块
import wordcloud                   #导入词云图模块
from scipy.misc import imread      #从scipy.misc模块导入imread函数
from matplotlib import colors      #从matplotlib模块导入colors函数
# 读取文本文件
str1 = open('mr.txt','r').read()   #ycy.txt可以改成自己的文件
cut_text = jieba.cut(str1)         #分词处理
word = ' '.join(cut_text)          #以空格分割文本
#红黑色值
color_list=['black','red']
#多种颜色
'''color_list=['LightCoral','RosyBrown','IndianRed','Red','Brown','FireBrick'
            ,'DarkRed','Maroon','Gainsboro','LightGray'
            ,'Silver','DarkGray','Gray','DimGray','Black']'''
colormap=colors.ListedColormap(color_list) #matplotlib色图
#外星人版
pic = imread('外星人1.png')        #读取图片
wc = wordcloud.WordCloud(
    mask=pic,                      #背景图形,如果根据图片绘制，则需要设置
    font_path='simhei.ttf',        #可以改成自己喜欢的字体
    background_color='white',      #词云图背景颜色可以换成自己喜欢的颜色
    colormap=colormap
    )
wc.generate(word)                  #生成词云
#显示词云图
plt.imshow(wc)
plt.axis('off')
plt.show()
