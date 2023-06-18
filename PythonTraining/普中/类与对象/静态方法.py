# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-03 21:30
"""
class Example:
    num = 10
    @staticmethod
    def static_method():
        print(f"类属性值为:{Example.num}")
        print('静态方法')

example = Example()
example.static_method()
Example.static_method()