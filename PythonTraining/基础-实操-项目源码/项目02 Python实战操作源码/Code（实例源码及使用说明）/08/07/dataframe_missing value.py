#返回缺失值个数以及最大最小值
import pandas as pd
datafile='../data/TB2018.xlsx'  #原始数据,第一行为属性标签
resultfile = '../data/view.xlsx' #数据探索结果表
data = pd.read_excel(datafile, encoding = 'utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
data=data[['订单付款时间','买家会员名','买家实际支付金额']]
view = data.describe(percentiles = [], include = 'all').T #包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（如1/4分位数、中位数等）；T是转置，转置后更方便查阅
view['null'] = len(data)-view['count'] #describe()函数自动计算非空值数，需要手动计算空值数
view = view[['null', 'max', 'min']]
view.columns = [u'空值数', u'最大值', u'最小值'] #表头重命名
view.to_excel(resultfile) #导出结果
df1 = pd.read_excel(datafile)
#去除空值，订单付款时间非空值才保留
#去除买家实际支付金额为0的记录
df1=df1[df1['订单付款时间'].notnull() & df1['买家实际支付金额'] !=0]  
print(df1)

