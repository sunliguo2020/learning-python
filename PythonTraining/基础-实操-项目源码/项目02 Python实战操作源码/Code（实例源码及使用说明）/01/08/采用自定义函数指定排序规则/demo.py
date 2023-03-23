# *_* coding : UTF-8 *_*

# 文件名称   ：demo01.py
# 开发工具   ：PyCharm
def rulesort(elem):  # 定义排序规则
    return elem["python"]

list_dict = [{"name":"无语","python":99,"c":89},
            {"name":"wgh","python":100,"c":80},
            {"name":"琦琦","python":95,"c":97},
            {"name":"明日","python":91,"c":96}]
print("对列表排序前：")
for d in list_dict:
    print(d)
list_dict.sort(key = rulesort ,reverse = True)  # 降序排列
print("对列表排序后：")
for d in list_dict:
    print(d)



