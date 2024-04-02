# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/2 20:59
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Task:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())
