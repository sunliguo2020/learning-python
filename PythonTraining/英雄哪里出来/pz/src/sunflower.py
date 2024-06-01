# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:50
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import pygame

from src import objectbase
from src.sunlight import SunLight


class SunFlower(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.hasSunLight = False

    def preSummon(self):
        """

        """
        self.hasSunLight = True

    def hasSummon(self):
        """

        @return:
        """
        return self.hasSunLight

    def doSummon(self):
        """
        生成召唤物
        @return:
        """
        if self.hasSummon():
            self.hasSunLight = False
            return SunLight(2, (self.pos[0] + 20, self.pos[1] - 10))
