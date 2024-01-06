# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 13:03
"""
import asyncio
import time


async def run(i):
    print('lucky is a good man', i)
    # 模拟一个耗时IO
    await asyncio.sleep(2)
    print('lucky is a  nice man', i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = []
    t1 = time.time()

    for url in range(1, 5):
        coroutinue = run(url)
        task = asyncio.ensure_future(coroutinue)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))

    t2 = time.time()
    print(f'总耗时：{t2 - t1}')
