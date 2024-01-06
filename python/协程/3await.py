# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 16:33
"""
import asyncio


async def func():
    print("来玩啊")
    response = await asyncio.sleep(2)
    print('结束', response)


asyncio.run(func())
