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

from objectBase import ObjectBase

pygame.init()

DS = pygame.display.set_mode(GAME_SIZE)
back_image = Image(PATH_BACK, 0, (0, 0), GAME_SIZE, 0)
zom = ObjectBase('../pic/zombie/0/%d.png', 0, (1080, 200), (100, 128), 15)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DS.fill((255, 255, 255))
    back_image.draw(DS)
    zom.draw(DS)
    zom.update()
    pygame.display.update()
