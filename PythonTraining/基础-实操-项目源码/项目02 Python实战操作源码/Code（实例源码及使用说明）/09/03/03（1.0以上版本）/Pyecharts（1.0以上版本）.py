import pandas as pd
import numpy
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
aa =r'TB1.xls'
df = pd.DataFrame(pd.read_excel(aa))
df1=df[['订单付款时间','买家实际支付金额']]
df1 = df1.set_index('订单付款时间')  #将“订单付款时间”设置为索引
df2=df1.resample('M').sum().to_period('M')
x=["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
#转列表取整数
y=df2['买家实际支付金额'].apply(numpy.round).values.tolist()
#主题风格和背景颜色
bar=Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK,bg_color='green'))
#图表标题
bar.set_global_opts(title_opts=opts.TitleOpts(title="月销量分析"))
#图表x轴、y轴
bar.add_xaxis(x)
bar.add_yaxis("",y)
#图表标记最大值、最小值
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                    markpoint_opts=opts.MarkPointOpts(
                        data=[opts.MarkPointItem(type_="max", name="最大值"),
                              opts.MarkPointItem(type_="min", name="最小值")]))
#图表显示平均线
bar.set_series_opts(markline_opts=opts.MarkLineOpts(
                        data=[opts.MarkLineItem(type_="average", name="平均值")]))
        
bar.render('sales1.html')

