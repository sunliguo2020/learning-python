# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 13:58
"""
import asyncio


async def run(url):
    print('异步任务开始')
    await asyncio.sleep(2)
    print('异步任务结束')
    return url


def call_back(f):
    print('返回值：', f.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task_list = []
    for url in ['百度', 'ali', 'jingdong']:
        coroutinue = run(url)
        task = loop.create_task(coroutinue)
        task.add_done_callback(call_back)
        task_list.append(task)
    loop.run_until_complete(asyncio.wait(task_list))