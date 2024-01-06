# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 13:25
"""
import asyncio


async def run(i):
    print('我是协程开始', i)
    await  asyncio.sleep(2)
    print('我是协程结束', i)
    return '返回值'


# 回调函数
def call_back(f):
    print(f.result())  # 获取返回值


if __name__ == '__main__':
    c = run(1)
    # 创建任务
    task = asyncio.ensure_future(c)
    # 给任务添加回调
    task.add_done_callback(call_back)
    loop = asyncio.get_event_loop()
    # 将任务放到事件循环中
    loop.run_until_complete(task)
