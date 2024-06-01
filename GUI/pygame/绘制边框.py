# -*- coding: utf-8 -*-
"""
 @Time : 2024/6/1 11:16
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((800, 600))

# 加载一个 Sprite 图像
sprite_image = pygame.image.load('0.png').convert_alpha()


# 创建一个 Sprite 类
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(400, 300))  # 设置 Sprite 的初始位置

    def draw_border(self, surface, color=(255, 0, 0), width=2):
        # 在 Sprite 的矩形区域周围绘制一个边框
        pygame.draw.rect(surface, color, self.rect, width)

    # 创建一个 Sprite 实例


my_sprite = Sprite(sprite_image)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # 填充屏幕为黑色
    screen.fill((0, 0, 0))

    # 绘制 Sprite 的图像
    screen.blit(my_sprite.image, my_sprite.rect.topleft)

    # 绘制 Sprite 的边框
    my_sprite.draw_border(screen, color=(255, 255, 0))  # 使用黄色边框

    # 更新屏幕显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()