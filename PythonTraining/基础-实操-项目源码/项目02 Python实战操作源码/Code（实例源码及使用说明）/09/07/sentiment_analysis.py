from snownlp import SnowNLP
#from snownlp import sentiment #加载情感分析模块
import pandas as pd #加载pandas
import matplotlib.pyplot as plt

aa ='../data/京东评论.xls'
df=pd.read_excel(aa) #读取文本数据
df1=df.iloc[:,3] #提取所有数据
print(df1)

values=[SnowNLP(i).sentiments for i in df1] #遍历每条评论进行预测

#输出积极的概率，大于0.5积极的，小于0.5消极的

#保存预测值
myval=[]
good=0
bad=0
for i in values:
   if (i>=0.5):
       myval.append("正面")
       good=good+1
   else:
       myval.append("负面")
       bad=bad+1

df['预测值']=values
df['评价类别']=myval  
df.to_excel('result2.xls')
rate=good/(good+bad)
print('好评率','%.f%%' % (rate * 100)) #格式化为百分比

y=values
plt.rc('font', family='SimHei', size=10)
plt.plot(y, marker='o', mec='r', mfc='w',label=u'评价分值')
plt.xlabel('用户')
plt.ylabel('评价分值')

plt.legend()  # 让图例生效

plt.title('京东评论情感分析',family='SimHei',size=14,color='blue')
plt.show()


