# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-11-24 20:42
"""


class Tools:
    # 定义类属性
    count = 0

    def __init__(self):
        # 创建对象 会自动调用 init 方法, 创建对象后, count 的值应该 + 1
        Tools.count += 1

    def self_set_count(self):
        # 使用 self 在设置类属性的时候,会在 self 对应的实例化对象中添加一个与类属性count同名且值相同的count属性,
        #
        # 通过self设置类属性
        self.count += 1

    def self_get_count(self):  # self代表当前对象
        # 通过self访问类属性
        return self.count

    @classmethod
    def class_get_count(cls):  # cls代表当前类
        # 通过cls访问类属性
        return cls.count

    @classmethod
    def class_set_count(cls):
        # 通过cls设置类属性
        cls.count += 1


# 创建对象后, count 的值应该 + 1
self_count = Tools()  # count = 1
print(self_count.count)
self2_count = Tools()  # count = 2
print(self_count.count)
print(self2_count.count)

# 调用self_set_count方法, count = 3
self_count.self_set_count()
# 通过self查看count的值
print(f'count:{self_count.self_get_count()}')  # count = 3

# 通过cls查看count的值
print(f'count:{Tools.class_get_count()}')  # count =2
