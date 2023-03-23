import matplotlib.pyplot as plt
import numpy as np
# 为柱状图添加标注
def label(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x()+bar.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

plt.rcParams['font.sans-serif'] = ['SimHei']	# 显示中文
plt.rcParams['axes.unicode_minus'] = False	# 显示负号
# 生成画布
plt.figure()
# 横坐标缴费年份
name_list = ['15年','20年','25年','30年','35年','40年','45年','50年']
#养老金的钱分两部分：基础养老金、个人账户养老金
#基础养老金（当地）：上年度在岗职工月平均工资和本人指数化月平均缴费工资的平均值为基数，缴费每满1年发给1%
#个人账户养老金=个人账户储存额/计发月数。65退休为101个月
# 预测领取养老金（保守算法,缴费工资4500、增长率3%）
myMoney_list=[]
#缴费年限
years=[15,20,25,30,35,40,45,50]
#月平均工资
pay=4500
local_pay=6000
#经济增长率，工资增长率
GDP_rate=0.07
#未来个人养老金账户余额利息（银行利率）
Bank_rate=0.03
for i in years:
  #个人养老金
  person=(pay*(1+GDP_rate+Bank_rate))*i*0.08*12/101
  #基础养老金(当地)
  basis=((local_pay+pay)/2)*i*0.01
  myMoney_list.append(person+basis)
print(myMoney_list)
y=myMoney_list
x=range(len(name_list))
print(x)
label(plt.bar(x,y,color='CornflowerBlue',tick_label=name_list))
list1=[]
#增长率计算(工资)
for i in range(len(y)-1):
    list1.append((y[i+1]-y[i])/y[i])
print(list1)
#设置图表标题
plt.title('养老金分析')
plt.show()
