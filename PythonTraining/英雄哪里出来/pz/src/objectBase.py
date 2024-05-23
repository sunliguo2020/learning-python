# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:46
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import image


class ObjectBase(image.Image):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super(ObjectBase, self).__init__(pathFmt, pathIndex, pos, size, pathIndexCount)

    def update(self):
        self.checkImageIndex()
        self.checkPosition()

    def checkImageIndex(self):
        pass

    def checkPosition(self):
        pass
