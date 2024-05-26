# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:47
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import pygame


class Image(pygame.sprite.Sprite):
    """

    """

    def __init__(self, pathFmt: str, pathIndex, pos: tuple, size: tuple = None, pathIndexCount=0):
        """

        @param pathFmt: 图片路径模版
        @param pathIndex: 图片路径索引
        @param pos: 位置
        @param size: 大小，元组
        @param pathIndexCount: 图片总数
        """
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.pos = list(pos)
        self.size = size
        self.pathIndexCount = pathIndexCount

        self.updateImage()

    def updateImage(self):
        """
        更新
        1、如果pahtIndexCount为0,则直接使用pathFmt为图片路径
        2、不为0,则为路径格式字符串。
        @return:
        """
        path = self.pathFmt
        if self.pathIndexCount != 0:
            path = path % self.pathIndex
            print(f"path:{path}")

        self.image = pygame.image.load(path)

        if self.size:
            # 改变图片大小
            self.image = pygame.transform.scale(self.image, self.size)

    def updateSize(self, size):
        self.size = size
        self.updateImage()

    def updateIndex(self, pathIndex):
        print(f"调用updateIndex：{pathIndex}")
        self.pathIndex = pathIndex
        self.updateImage()

    def getRect(self):
        """
        从某个类（可能是表示图像、精灵或其他图形对象的类）中获取一个矩形区域（rect）。
        这个矩形区域通常用于碰撞检测、定位或其他图形操作.
        @return:
        """
        # 调用get_rect()方法，并返回一个矩形区域（rect），该区域与图像的尺寸相同，但默认位置是(0, 0)。
        rect = self.image.get_rect()
        # 指定位置
        rect.x, rect.y = self.pos
        return rect

    def doLeft(self):
        # 往左移动
        self.pos[0] -= 1

    def draw(self, ds: pygame.display):
        """
        blit()函数的作用 ：
            将一个图像（通常是一个 Surface 对象）绘制（或“blit”）到另一个 Surface 或屏幕上的指定位置
        @param ds:
        @return:
        """
        print(f"正在绘制：{self.image},位置：{self.getRect()}")
        ds.blit(self.image, self.getRect())
