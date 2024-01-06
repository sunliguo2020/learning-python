# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 13:38
"""
import asyncio
import time


async def run(url):
    print(f'{url}开始')
    await  asyncio.sleep(2)
    print(f"{url}结束")


if __name__ == '__main__':
    t1 = time.time()
    task_list = []

    for i in range(3):
        c = run(i)
        # 创建任务
        task = asyncio.ensure_future(c)
        task_list.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    print(time.time() - t1)
