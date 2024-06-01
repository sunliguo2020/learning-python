# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:49
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import random
import time
from typing import List

import pygame.mouse

import peashooter
from src import objectbase, data_object
from src.image import Image
from const import *
from src.sunflower import SunFlower
from zombiebase import ZombieBase


class Game:
    def __init__(self, ds):
        self.ds = ds
        self.back_img = Image(PATH_BACK, 0, (0, 0), GAME_SIZE, 0)
        self.plants = []
        self.zombies = []
        # 召唤物
        self.summons: List[objectbase.ObjectBase] = []
        self.hasPlant = []

        self.zombieGenerateTime = 0
        self.gold = 100
        self.goldFont = pygame.font.Font(None, 60)

        self.zombie = 0
        self.zombieFont = pygame.font.Font(None, 60)

        for i in range(GRID_COUNT[0]):
            col = []
            for j in range(GRID_COUNT[1]):
                col.append(0)
            self.hasPlant.append(col)

    def update(self):
        """

        @return:
        """
        for plant in self.plants:
            plant.update()
            # 产生召唤物
            if plant.hasSummon():
                summon = plant.doSummon()
                self.summons.append(summon)
        # 产生僵尸
        if time.time() - self.zombieGenerateTime > ZOMBIE_BORN_CD:
            self.zombieGenerateTime = time.time()
            self.addZombie(ZOMBIE_BORN_X, random.randint(0, GRID_COUNT[1] - 1))

        for summon in self.summons:
            summon.update()

        for zombie in self.zombies:
            zombie.update()

        self.checkSummonVSZombie()

        # 超出屏幕范围，销毁召唤物
        for summon in self.summons:
            if summon.getRect().x > GAME_SIZE[0] or summon.getRect().y > GAME_SIZE[1]:
                print(f'销毁召唤物')
                self.summons.remove(summon)
                break

        print(f"僵尸数目：{len(self.zombies)}")
        print(f"子弹数目：{len(self.summons)}")

    def checkSummonVSZombie(self):
        """
        召唤物和僵尸战斗
        @return:
        """
        for summon in self.summons:
            for zombie in self.zombies:
                if summon.isCollide(zombie):
                    self.fight(summon, zombie)
                    if zombie.hp <= 0:
                        self.zombies.remove(zombie)
                        self.zombie += 1
                    if summon.hp <= 0:
                        self.summons.remove(summon)
                    return

    def renderFont(self):
        textImage = self.goldFont.render(f"Gold:{str(self.gold)}", True, (0, 0, 0))
        self.ds.blit(textImage, (13, 23))
        textImage = self.goldFont.render(f"Gold:{str(self.gold)}", True, (255, 255, 255))
        self.ds.blit(textImage, (10, 20))

        textImage = self.zombieFont.render(f"Score:{str(self.zombie)}", True, (0, 0, 0))
        self.ds.blit(textImage, (13, 83))
        textImage = self.zombieFont.render(f"Score:{str(self.zombie)}", True, (255, 255, 255))
        self.ds.blit(textImage, (10, 80))

    def draw(self):
        """

        @return:
        """
        self.back_img.draw(self.ds)
        # 绘制植物
        for plant in self.plants:
            plant.draw(self.ds)
        # 绘制召唤物
        for summon in self.summons:
            summon.draw(self.ds)
        # 僵尸
        for zombie in self.zombies:
            zombie.draw(self.ds)

        self.renderFont()

    def getIndexBypos(self, mousePos):
        """

        @param mousePos:
        @return:
        """
        x = (mousePos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (mousePos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y

    def addSunFlower(self, x, y):
        """
        种植向日葵
        @param x:
        @param y:
        @return:
        """

        self.hasPlant[x][y] = 1

        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]

        sf = SunFlower(SUNFLOWER_ID, pos)

        print(f"向日葵位置:{pos},x:{x},y:{y}")

        self.plants.append(sf)

    def addPeaShooter(self, x, y):
        """
        种植豌豆射手
        @param x:
        @param y:
        @return:
        """

        self.hasPlant[x][y] = 1

        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]

        sf = peashooter.PeaShooter(PEASHOOTER_ID, pos)

        print(f"豌豆射手位置:{pos},x:{x},y:{y}")

        self.plants.append(sf)

    def addZombie(self, x, y):
        """
        僵尸
        @param x:
        @param y:
        @return:
        """

        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = ZombieBase(ZOMBIE_ID, pos)

        print(f"僵尸位置:{pos},x:{x},y:{y}")

        self.zombies.append(sf)

    def fight(self, a, b):
        while True:
            a.hp -= b.attack
            b.hp -= a.attack
            if b.hp <= 0:
                return True
            if a.hp <= 0:
                return False
        return False

    def checkLoot(self, mousePos):
        """
        捡阳光
        @return:
        """
        for summon in self.summons:
            if not summon.canLoot():
                continue
            rect = summon.getRect()
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                self.gold += summon.getPrice()

                return True
        return False

    def checkAddPlant(self, mousePos, objId):
        """
        种植某种植物
        @param mousePos:鼠标点击坐标
        @param objId:
        @return:
        """
        # 根据鼠标点击坐标获取可以放置植物的坐标位置
        x, y = self.getIndexBypos(mousePos)

        if x < 0 or x >= GRID_COUNT[0]:
            return
        if y < 0 or y >= GRID_COUNT[1]:
            return

        if self.gold < data_object.data.get(objId)['PRICE']:
            return

        if self.hasPlant[x][y] == 1:
            return

        self.gold -= data_object.data.get(objId)['PRICE']
        if objId == SUNFLOWER_ID:
            self.addSunFlower(x, y)
        elif objId == PEASHOOTER_ID:
            self.addPeaShooter(x, y)

    def mouseClickHandler(self, btn):
        """
        处理鼠标点击事件
        @param btn:
        @return:
        """
        # 鼠标点击位置
        mousePos = pygame.mouse.get_pos()
        if not self.checkLoot(mousePos):
            if btn == 1:
                self.checkAddPlant(mousePos, SUNFLOWER_ID)
            elif btn == 3:
                self.checkAddPlant(mousePos, PEASHOOTER_ID)
