# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 13:10
如果想要让生成器继续向下运行，我们可以使用next或者send
相同点：
    都会让生成器继续向下运行
    如果运行时，遇不见yield，那么都会产生异常
不同点：
    next只会让 运行继续开始
    而
    send除了可以让其开始运行之外，还可以将某个数据携带过去。
"""
