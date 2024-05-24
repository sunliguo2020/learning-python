# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:45
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import sys

import pygame
from pygame.locals import QUIT
from image import Image
from const import *

from objectbase import ObjectBase
from zombiebase import ZombieBase
from peabullet import PeaBulletBase
pygame.init()

DS = pygame.display.set_mode(GAME_SIZE)
back_image = Image(PATH_BACK, 0, (0, 0), GAME_SIZE, 0)
zom = ZombieBase(1, (1080, 200))
pb = PeaBulletBase(0, (0, 200))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DS.fill((255, 255, 255))
    back_image.draw(DS)
    zom.draw(DS)
    zom.update()

    pb.draw(DS)
    pb.update()
    pygame.display.update()
