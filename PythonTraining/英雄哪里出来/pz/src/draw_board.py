# -*- coding: utf-8 -*-
"""
 @Time : 2024/6/2 10:26
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import pygame
import sys

# 窗口大小
GAME_SIZE = (1280, 600)
# 格数
GRID_COUNT = (9, 5)
# 每个单元格大小
GRID_SIZE = (76, 96)
# 最左上角坐标
LEFT_TOP = (230, 65)

# 初始化pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode(GAME_SIZE)

# 设置颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# 绘制棋盘函数
def draw_chessboard(screen, grid_count, grid_size, left_top):
    for i in range(grid_count[0]):
        for j in range(grid_count[1]):
            # 计算每个格子的左上角坐标
            grid_left_top = (left_top[0] + i * grid_size[0], left_top[1] + j * grid_size[1])
            # 绘制格子
            pygame.draw.rect(screen, BLACK if (i + j) % 2 == 0 else WHITE,
                             (grid_left_top, grid_size), 1)  # 1表示边框宽度


# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # 填充背景颜色
    screen.fill((200, 200, 255))

    # 绘制棋盘
    draw_chessboard(screen, GRID_COUNT, GRID_SIZE, LEFT_TOP)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)

# 退出pygame
pygame.quit()
sys.exit()
