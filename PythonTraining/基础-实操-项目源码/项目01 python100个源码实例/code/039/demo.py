#导入matplotlib模块pyplot函数并使用as给函数起个别名plt
import matplotlib.pyplot as plt    
import jieba                       #导入jieba分词模块
import wordcloud                   #导入词云图模块
from scipy.misc import imread      #导入imread函数
# 读取文本文件
str1 = open('ycy.txt','r').read()  #ycy.txt可以改成自己的文件
cut_text = jieba.cut(str1)         #分词处理
word = ' '.join(cut_text)          #以空格分割文本
pic = imread('ycy.png')           #读取图片
wd = wordcloud.WordCloud(
    mask=pic,                      #根据图片绘制词云图
    font_path='simhei.ttf',        #字体
    background_color='white'       #词云图背景颜色
    )
wd.generate(word)                  #生成词云
#显示词云图
plt.imshow(wd)
plt.axis('off')                   #关闭图表的x、y轴
plt.show()
