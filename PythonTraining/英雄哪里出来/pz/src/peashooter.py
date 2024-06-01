# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:50
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import time

from src import objectbase
import peabullet


class PeaShooter(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.hasBullet = False
        self.hasShoot = False

    def preSummon(self):
        """

        """
        self.hasShoot = True
        self.pathIndex = 0

    def hasSummon(self):
        """

        @return:
        """
        return self.hasBullet

    def doSummon(self):
        """
        产生召唤物
        @return:
        """
        if self.hasSummon():
            self.hasBullet = False
            return peabullet.PeaBullet(0, (self.pos[0] + self.size[0] - 10, self.pos[1] + 30))

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
        if idx == 8 and self.hasShoot:
            self.hasBullet = True

        if idx >= self.pathIndexCount:
            idx = 9

        self.updateIndex(idx)
