# *_* coding : UTF-8 *_*

# 文件名称   ：forecast.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块
from sklearn.svm import LinearSVR  # 导入回归函数


data = pandas.read_csv('data.csv')  # 读取csv数据文件
del data['Unnamed: 0']  # 将索引列删除
data.dropna(axis=0, how='any', inplace=True)  # 删除data数据中的所有空值
data['总价'] = data['总价'].map(lambda z: z.replace('万', ''))  # 将总价“万”去掉
data['总价'] = data['总价'].astype(float)  # 将房子总价转换为浮点类型
data['建筑面积'] = data['建筑面积'].map(lambda p: p.replace('平米', ''))  # 将建筑面价“平米”去掉
data['建筑面积'] = data['建筑面积'].astype(float)  # 将建筑面积转换为浮点类型
data_copy = data.copy()      # 拷贝数据
# print(data_copy[['户型', '建筑面积']].head())


data_copy[['室', '厅', '卫']] = data_copy['户型'].str.extract('(\d+)室(\d+)厅(\d+)卫')
data_copy['室'] = data_copy['室'].astype(float)  # 将房子室转换为浮点类型
data_copy['厅'] = data_copy['厅'].astype(float)  # 将房子厅转换为浮点类型
data_copy['卫'] = data_copy['卫'].astype(float)  # 将房子卫转换为浮点类型
# print(data_copy[['室','厅','卫']].head())          # 打印“室”、“厅”、“卫”数据

del data_copy['小区名字']
del data_copy['户型']
del data_copy['朝向']
del data_copy['楼层']
del data_copy['装修']
del data_copy['区域']
del data_copy['单价']
data_copy.dropna(axis=0, how='any', inplace=True)  # 删除data数据中的所有空值
# 获取“建筑面积”小于300平米的房子信息
new_data = data_copy[data_copy['建筑面积'] < 300].reset_index(drop=True)
# print(new_data.head())                                  # 打印处理后的头部信息


#  添加自定义预测数据
new_data.loc[2505] = [None, 88.0, 2.0, 1.0, 1.0]
new_data.loc[2506] = [None, 136.0, 3.0, 2.0, 2.0]
data_train=new_data.loc[0:2504]
x_list = ['建筑面积',  '室', '厅', '卫']    # 自变量参考列
data_mean = data_train.mean()               # 获取平均值
data_std = data_train.std()                 # 获取标准偏差
data_train = (data_train - data_mean) / data_std  # 数据标准化
x_train = data_train[x_list].values  # 特征数据
y_train = data_train['总价'].values  # 目标数据，总价
linearsvr = LinearSVR(C=0.1)  # 创建LinearSVR()对象
linearsvr.fit(x_train, y_train)      # 训练模型
# 标准化特征数据
x = ((new_data[x_list] - data_mean[x_list]) / data_std[x_list]).values
# 添加预测房价的信息列
new_data[u'y_pred'] = linearsvr.predict(x) * data_std['总价'] + data_mean['总价']
print('真实值与预测值分别为：\n', new_data[['总价', 'y_pred']])