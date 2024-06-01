# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:45
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import sys

import pygame
from pygame.locals import QUIT

from const import *

from game import Game

pygame.init()

DS = pygame.display.set_mode(GAME_SIZE)
game = Game(DS)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouseClickHandler(event.button)

    DS.fill((255, 255, 255))
    game.draw()
    game.update()
    pygame.display.update()
