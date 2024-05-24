# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:50
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import objectbase
from const import *


class PeaBulletBase(objectbase.ObjectBase):
    def checkPosition(self):
        b = super().checkPosition()
        if b:
            self.pos[0] += 4
            if self.pos[0] > GAME_SIZE[0]:
                self.pos[0] = 0
        else:
            return b
