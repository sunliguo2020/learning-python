# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 13:13
"""
import asyncio


async def run():
    print('我是run函数')


if __name__ == '__main__':
    c = run()
    print(c)
    asyncio.run(c)
