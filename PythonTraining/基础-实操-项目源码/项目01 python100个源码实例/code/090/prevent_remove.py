import re
import os
import time
# pip install itchat
import itchat
import platform
from itchat.content import *


msg_info = {}
face_package = None


# 处理接收到的信息
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True, isMpChat=True)
def handle_rsg(msg):
    global face_package
    # 接收消息的时间
    msg_time_receive = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 发信人
    try:
        msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    except:
        msg_from = 'WeChat Official Accounts'
    # 发信时间
    msg_time_send = msg['CreateTime']
    # 信息ID
    msg_id = msg['MsgId']
    msg_content = None
    msg_link = None
    # 文本或者好友推荐
    if msg['Type'] == 'Text' or msg['Type'] == 'Friends':
        msg_content = msg['Text']
        print('[Text/Friends]: %s' % msg_content)
    # 附件/视频/图片/语音
    elif msg['Type'] == 'Attachment' or msg['Type'] == "Video" or msg['Type'] == 'Picture' or msg['Type'] == 'Recording':
        msg_content = msg['FileName']
        msg['Text'](str(msg_content))
        print('[Attachment/Video/Picture/Recording]: %s' % msg_content)
    # 推荐名片
    elif msg['Type'] == 'Card':
        msg_content = msg['RecommendInfo']['NickName'] + '的推荐名片，'
        if msg['RecommendInfo']['Sex'] == 1:
            msg_content += '性别男。'
        else:
            msg_content += '性别女。'
        print('[Card]: %s' % msg_content)
    # 位置信息
    elif msg['Type'] == 'Map':
        x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度:" + x.__str__() + ", 经度:" + y.__str__()
        else:
            msg_content = r"" + location
        print('[Map]: %s' % msg_content)
    # 分享的音乐/文章
    elif msg['Type'] == 'Sharing':
        msg_content = msg['Text']
        msg_link = msg['Url']
        print('[Sharing]: %s' % msg_content)
    msg_info.update(
            {
                msg_id: {
                    "msg_from": msg_from,
                    "msg_time_send": msg_time_send,
                    "msg_time_receive": msg_time_receive,
                    "msg_type": msg["Type"],
                    "msg_content": msg_content,
                    "msg_link": msg_link
                }
            }
        )
    face_package = msg_content


# 监听是否有消息撤回
@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
def monitor(msg):
    if '撤回了一条消息' in msg['Content']:
        recall_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
        recall_msg = msg_info.get(recall_msg_id)
        print('[Recall]: %s' % recall_msg)
        # 表情包
        if len(recall_msg_id) < 11:
            itchat.send_file(face_package, toUserName='filehelper')
        else:
            msg_prime = '---' + recall_msg.get('msg_from') + '撤回了一条消息---\n' \
                        '消息类型：' + recall_msg.get('msg_type') + '\n' \
                        '时间：' + recall_msg.get('msg_time_receive') + '\n' \
                        '内容：' + recall_msg.get('msg_content')
            if recall_msg['msg_type'] == 'Sharing':
                msg_prime += '\n链接：' + recall_msg.get('msg_link')
            itchat.send_msg(msg_prime, toUserName='filehelper')
            if recall_msg['msg_type'] == 'Attachment' or recall_msg['msg_type'] == "Video" or recall_msg['msg_type'] == 'Picture' or recall_msg['msg_type'] == 'Recording':
                file = '@fil@%s' % (recall_msg['msg_content'])
                itchat.send(msg=file, toUserName='filehelper')
                os.remove(recall_msg['msg_content'])
            msg_info.pop(recall_msg_id)


if __name__ == '__main__':
    if platform.platform()[:7] == 'Windows':
        itchat.auto_login(enableCmdQR=False, hotReload=True)
    else:
        itchat.auto_login(enableCmdQR=True, hotReload=True)
    itchat.run()
