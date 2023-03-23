# pip install -U wxpy
from wxpy import *

# 扫码登陆
bot = Bot()

# 初始化图灵机器人 (API key 申请: http://tuling123.com)，并认证
# '6b61f29cdb694a8eb18c84ed97beb750' '20ee91ffc00f42298bb02f7f290bf74d'
tuling = Tuling(api_key='759e94b5631f4cc9d9de36b1a3e0811')

# 设置不自动回复的群和好友
boring_group = bot.groups().search('明日科技')[0]
boring_group1 = bot.groups().search('明日科技')[0]
jt = bot.friends().search('Z')[0]

# 打印所有群
mygroup=bot.groups()
print(mygroup)


# 不自动回复指定的群消息和好友消息
@bot.register([boring_group, boring_group1, jt])
def ignore(msg):
    print('ignore is running')
    print(msg)
    # 啥也不做
    return


# 打印指定的群消息
@bot.register([boring_group, boring_group1])
def just_print(msg):
    print(msg)
    print('just_print is running')


# 回复@的群聊消息和个人消息
@bot.register(msg_types=TEXT)  # 注册消息类型为文本消息
def auto_reply(msg):
    print('auto_reply is running')
    if isinstance(msg.chat, Group) and not msg.is_at:  # 判断是否是@的消息和个人消息
        return  # 如果不是@消息，什么也不做
    else:
        # tuling.do_reply(msg)  # 图灵自动回复消息
        print(msg)  # 打印消息
        print(tuling.do_reply(msg))  # 打印并回复消息
        # return '收到消息:{}({})'.format(msg.text, msg.type)  # 回复消息：收到消息：内容


embed()  # 堵塞线程，并进入 Python 命令行
