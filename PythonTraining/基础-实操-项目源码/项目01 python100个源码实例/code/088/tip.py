# pip install itchat
import itchat
# pip install pygame
import pygame


def alarm():
    pygame.mixer.init()
    pygame.mixer.music.load('tip.mp3')
    pygame.mixer.music.play()


# 监控群聊是否有红包
@itchat.msg_register('Note', isGroupChat=True)
def get_tip_group(msg):
    if u'收到红包' in msg['Text']:
        print('[INFO]: %s ' % msg['Text'])
        alarm()


# 监控个人红包
@itchat.msg_register('Note', isGroupChat=False)
def get_tip(msg):
    if u'收到红包' in msg['Text']:
        print('[INFO]: %s ' % msg['Text'])
        alarm()


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
    itchat.logout()




