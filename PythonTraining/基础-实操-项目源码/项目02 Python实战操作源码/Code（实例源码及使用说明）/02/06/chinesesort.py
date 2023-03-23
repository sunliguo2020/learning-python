from xpinyin import Pinyin  # 导入汉字转拼音模块


def my_sort(wordlist):  # 指定要排序的列表
    pin = Pinyin()   # 创建汉字转拼音对象
    temp = []   # 保存转换结果的空列表
    for item in wordlist:  # 遍历品牌名称列表
        temp.append((pin.get_pinyin(item), item)) # 将汉字的拼音和汉字放到一个元组中，再添加到列表中
    temp.sort()   # 对列表进行排序
    result = []   # 保存排序后的列表
    for i in range(len(temp)):  # 遍历排序后的列表
        result.append(temp[i][1]) # 取出汉字保存到新列表中
    return result  # 返回排序后的列表

print(my_sort(['华为', '小米' , '苹果', '三星' ]))  # 调用函数时指定一个品牌名称列表


