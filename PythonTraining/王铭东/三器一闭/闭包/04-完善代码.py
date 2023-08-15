# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 18:30
"""


def who(name):
    def do(content):
        print(f"{name}:{content}")

    return do


zhangsan = who('张三')
lisi = who('李四')
zhangsan('你努力了吗？')
lisi('为啥努力？')
zhangsan('你确定不努力吗?')
lisi('嗯，确定!')
