# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 'room_name'从URL路由中获取参数chat/routing.py ，打开与消费者的WebSocket连接。
        # 每个使用者都有一个范围，其中包含有关其连接的信息，
        # 特别是包括URL路由中的任何位置或关键字参数以及当前经过身份验证的用户
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # 直接从用户指定的房间名称构造Channels组名称，不进行任何引用或转义。
        # 组名只能包含字母，数字，连字符和句点。
        # 因此，此示例代码将在具有其他字符的房间名称上失败。
        self.room_group_name = 'chat_%s' % self.room_name

        # 进入房间
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # 接受WebSocket连接。
        # 如果不在connect（）方法中调用accept（），则拒绝并关闭连接。
        # 如果您选择接受连接，建议将accept（）作为connect（）中的最后一个操作调用。
        await self.accept()

    async def disconnect(self, close_code):
        # 离开房间
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 从WebSocket接收信息
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 发送信息到房间
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # 从房间接收信息
    async def chat_message(self, event):
        message = event['message']

        # 发送信息到WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
