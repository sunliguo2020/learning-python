# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:46
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import time

import data_object
import image


class ObjectBase(image.Image):
    """

    """

    def __init__(self, id, pos):
        """

        @param id:
        @param pos: 初始位置
        """
        self.id = id
        self.preIndexTime = 0
        self.prePositionTime = 0
        self.preSummonTime = 0
        self.hp = self.getData()['HP']
        self.attack = self.getData()['ATT']

        super(ObjectBase, self).__init__(self.getData()['PATH'],
                                         0,
                                         pos,
                                         self.getData()['SIZE'],
                                         self.getData()['IMAGE_INDEX_MAX'])

    def getData(self):
        return data_object.data[self.id]

    def update(self):
        self.checkSummon()
        self.checkImageIndex()
        self.checkPosition()

    def getIndexCD(self):
        """
        动画间隔时间
        获取当前对象动画的帧切换冷却时间（Cooldown Duration）
        这个冷却时间通常用来控制动画的播放速度，即两次帧切换之间的最小时间间隔
        @return:
        """
        return self.getData()['IMAGE_INDEX_CD']

    def getSummonCD(self):
        return self.getData()['SUMMON_CD']

    def getPositionCD(self):
        return self.getData()['POSITION_CD']

    def getSpeed(self):
        return self.getData()['SPEED']

    def getPrice(self):
        return self.getData()['PRICE']

    def canLoot(self):
        return self.getData()['CAN_LOOT']

    def isCollide(self, other):
        """
        碰撞检测
        @param other:
        @return:
        """
        return self.getRect().colliderect(other.getRect())

    def checkImageIndex(self):
        """
        实现帧动画
        实现帧动画的更新。
        具体来说，它负责根据一定的时间间隔来更新对象的图像索引（即当前显示的图像帧），
        从而创建动画效果。
        @return:
        """
        if time.time() - self.preIndexTime <= self.getIndexCD():
            return
        self.preIndexTime = time.time()

        idx = self.pathIndex + 1

        if idx >= self.pathIndexCount:
            idx = 0

        self.updateIndex(idx)

    def checkPosition(self):
        """
        改变位置
        @return:
        """
        if time.time() - self.prePositionTime <= self.getPositionCD():
            return False
        self.prePositionTime = time.time()

        speed = self.getSpeed()

        self.pos = self.pos[0] + speed[0], self.pos[1] + speed[1]

        return True

    def checkSummon(self):
        """

        @return:
        """
        if time.time() - self.preSummonTime <= self.getSummonCD():
            return
        self.preSummonTime = time.time()
        self.preSummon()

    def preSummon(self):
        pass

    def hasSummon(self):
        pass

    def doSummon(self):
        pass
