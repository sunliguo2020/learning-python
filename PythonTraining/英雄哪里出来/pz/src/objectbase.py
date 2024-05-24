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
        self.id = id
        self.preIndexTime = 0
        self.prePositionTime = 0
        super(ObjectBase, self).__init__(self.getData()['PATH'],
                                         0,
                                         pos,
                                         self.getData()['SIZE'],
                                         self.getData()['IMAGE_INDEX_MAX'])

    def getData(self):
        return data_object.data[self.id]

    def update(self):
        self.checkImageIndex()
        self.checkPosition()

    def getIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']

    def checkImageIndex(self):
        """
        实现帧动画
        @return:
        """
        if time.time() - self.preIndexTime <= self.getIndexCD():
            return
        self.preIndexTime = time.time()

        idx = self.pathIndex + 1
        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)

    def getPositionCD(self):
        return self.getData()['POSITION_CD']

    def checkPosition(self):
        if time.time() - self.prePositionTime <= self.getPositionCD():
            return False
        self.prePositionTime = time.time()
        return True
