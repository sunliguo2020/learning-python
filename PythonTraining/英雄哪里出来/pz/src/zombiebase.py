# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:50
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from src import objectbase


class ZombieBase(objectbase.ObjectBase):
    def checkPosition(self):
        b = super().checkPosition()
        if b:
            self.pos[0] -= 2.5
        else:
            return b

