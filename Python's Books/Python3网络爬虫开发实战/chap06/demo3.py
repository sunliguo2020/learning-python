# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/2 20:53
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


def callback(task):
    print('Status:', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print("task:", task)
