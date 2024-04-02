# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/2 21:08
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import asyncio
import requests
import time

stat_time = time.time()


async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response = await requests.get(url)
    print('Get response from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print("Cost time", end - stat_time)
