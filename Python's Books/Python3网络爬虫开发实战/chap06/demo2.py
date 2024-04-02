# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/2 20:47
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import asyncio


async def execute(x):
    print('Number', x)


coroutine = execute(1)
print('coroutine', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print('After calling loop')
