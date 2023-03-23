# *_* coding : UTF-8 *_*

# 文件名称   ：demo.py
# 开发工具   ：PyCharm
dictcar=[{'名称':'卡罗拉','销量':1181445},{'名称':'福特F系','销量':1080757},{'名称':'RAV4','销量':837624},{'名称':'思域','销量':823169},{'名称':'途观','销量':791275}]
dict1 = {'name': 'john', 'age': 23,'money':1200,'gender':'male'}
dict2 = {'name': 'anne', 'age': 22,'money':1500,'gender':'female'}
dict3 = {'name': 'james', 'age': 33,'money':578,'gender':'male'}
dict4 = {'name': 'nick', 'age': 46,'money':158,'gender':'male'}
dict5 = {'name': 'May', 'age': 18,'money':3210,'gender':'female'}    # 创建会员信息字典
lsitdc=[dict1,dict2,dict3,dict4,dict5]      # 创建二维会员信息字典
print(max(dictcar,key=lambda x:x['名称']))  # 输出结果为：{'名称': '途观', '销量': 791275}
# 输出结果为：{'名称': '卡罗拉', '销量': 1181445}
print(max(dictcar,key=lambda x:x['销量']))
# 输出结果为：{'name': 'anne', 'age': 22, 'money': 1500, 'gender': 'female'}
print(max(lsitdc,key=lambda item:(item['gender'] == 'female',item['age'])))
# 将积分超过500的会员年龄最大的会员输出，输出结果为：{'name': 'james', 'age': 33, 'money': 578, 'gender': 'male'}
print(max(lsitdc,key=lambda item:(item['money']>500,item['age'] )))
# 按积分输出最大者，输出结果为：{'name': 'May', 'age': 18, 'money': 3210, 'gender': 'female'}
print(max(lsitdc,key=lambda x:x['money']))
print(max(lsitdc,key=lambda x:x['age']).get('name'))  # 输出结果为：nick
