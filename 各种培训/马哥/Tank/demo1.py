import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class MainGame():
    window = None

    # BF
    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        pygame.display.init()
        # 窗口大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption("坦克大战")
        while True:
            # 设置窗口填充色
            pygame.display.update()

    # 结束游戏
    def endGame(self):
        pass


if __name__ == '__main__':
    MainGame().startGame()
