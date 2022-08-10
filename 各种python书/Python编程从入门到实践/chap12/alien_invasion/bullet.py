# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/27 12:47
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船所发射子弹的类"""

    def __init__(self, ai_game):
        """在飞船当前位置船舰一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
<<<<<<< HEAD
        self.settings = ai_game.settings
=======
<<<<<<< HEAD
<<<<<<< HEAD
        self.settings = ai_game.mySettings
=======
        self.settings = ai_game.settings
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172
=======
        self.settings = ai_game.settings
>>>>>>> 784558807086f17f7daecab3309a3392ab8b04c8
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
        self.color = self.settings.bullet_color

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.settings.bullet_speed
        #更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
