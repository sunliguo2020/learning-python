# -*- coding: utf-8 -*-
"""
 @Time : 2024/6/7 18:49
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import asyncio
import const


async def handle_client(reader, writer):
    """

    @param reader:
    @param writer:
    """
    data = await reader.read(const.MAX_BYTES)
    print(data)


async def main():
    """

    """
    server = await asyncio.start_server(handle_client, const.LISTEN_HOST, const.LISTEN_PORT)
    print('server start! listen port on 8888')
    async with server:
        await server.serve_forever()

asyncio.run(main())
