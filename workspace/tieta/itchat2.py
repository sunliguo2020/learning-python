import itchat
import tt_jiankongxiang

# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     #return (msg['Text'])
#     print(msg)
#     itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

# 处理文本类消息
# 包括文本、位置、名片、通知、分享
@itchat.msg_register(itchat.content.TEXT, itchat.content.MAP, itchat.content.CARD,\
                     itchat.content.NOTE)
def text_reply(msg):
    # 微信里，每个用户和群聊，都使用很长的ID来区分
    # msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    mymsg=tt_jiankongxiang.reply_jiangkongxiang_list()
    
    itchat.send('%s: %s' % (msg['Type'],mymsg), msg['FromUserName'])

# 处理多媒体类消息
# 包括图片、录音、文件、视频
@itchat.msg_register(itchat.content.PICTURE, itchat.content.RECORDING, \
                     itchat.content.ATTACHMENT, itchat.content.VIDEO)
def download_files(msg):
    # msg['Text']是一个文件下载函数
    # 传入文件名，将文件下载下来
    msg['Text'](msg['FileName'])
    # 把下载好的文件再发回给发送者
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 处理好友添加请求
@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text']) 
    # 加完好友后，给好友打个招呼
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# 处理群聊消息
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_text_reply(msg):
    print(msg)
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码

itchat.auto_login(hotReload=True)
itchat.run()
