# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 16:22
"""
import asyncio


async def func():
    print('快来搞我吧!')


result = func()

# 方式一
# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)

# 方式二：
asyncio.run(result)

