
from enum import IntEnum

import pygame

# 单格的宽度
square_size  =40
# 棋子大小
chess_size = square_size //2 -2
# 棋盘格式+1
web_broad = 15
# 棋盘长度
map_w = web_broad * square_size
# 棋盘高度
map_h = web_broad * square_size
# 按钮界面高度
info_w = 60
# 按钮长宽
button_w = 120
button_h = 45
#总窗口长宽
screen_w = map_w
screen_h = map_h + info_w

class MAP_ENUM(IntEnum):
    # 无人下
    be_empty = 0
    # 玩家一 执白
    player1 = 1
    # 玩家二 执黑
    player2 = 2
    # 出界
    out_of_range = 3

class Map:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height

        # 存储棋盘的二维数组
        self.map = [[ 0 for x in range(self.width)] for y in range(self.height)]

        # 记录步骤先后
        self.steps = []

    def get_init(self):
        """重置棋盘
        """
        for y in range(self.height):
            for x in range(self.width):
                self.map[y][x] =0
        self.steps = []
    
    def intoNextTurn(self,turn):
        """进入下一回合比赛中，交换下棋人

        Args:
            turn (_type_): _description_
        """
        if turn == MAP_ENUM.player1:
            return MAP_ENUM.player12
        else:
            return MAP_ENUM.player1
    def getLocate(self,x,y):
        """棋子具体位置

        Args:
            x (_type_): _description_
            y (_type_): _description_
        """
        map_x = x*square_size
        map_y = y*square_size

        return (map_x,map_y,square_size,square_size)

    def getIndex(self,map_x,map_y):
        """根据具体位置返回下标

        Args:
            map_x (_type_): _description_
            map_y (_type_): _description_
        """
        y = map_x // square_size
        x = map_x // square_size

        return (x,y)
    
    def isInside(self,map_x,map_y):
        """判断当前位置是否在棋盘的有效范围内
        """
        if(map_x<=0 or map_x >=map_w or map_y <=0 or map_y >=map_h):
            return False
        return True

    def isEmpty(self,x,y):
        """判断当前格式是否已经有棋子

        Args:
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        return (self.map[y][x] == 0 )
    
    def printChessPiece(self,screen):
        """绘制棋子


        Args:
            screen (_type_): _description_
        """
        player_one = (255,245,238)
        player_two = (41,36,33)

        player_color = [player_one,player_two]

        for i in range(len(self.steps)):
            x,y = self.steps[i]
            map_x ,map_y ,width,height = self.getLocate(x,y)
            pos,radius = (map_x +width//2,map_y+height//2),chess_size
            turn = self.map[y][x]
            # 画棋子
            pygame.draw.circle(screen,player_color[turn-1],pos,radius)

    def drawBoard(self,screen):
        color = (0,0,0)
        for y in range(self.height):
            # 画横线
            start_pos ,end_pos = (square_size//2,square_size//2+square_size*y),(map_w-square_size//2,square_size//2+square_size*y)
            pygame.draw.line(screen,color,start_pos,end_pos,1)

        for y in range(self.width):
            # 画竖线
            start_pos ,end_pos = (square_size//2+square_size*x,square_size//2),(map_w-square_size//2+square_size*x,map_h-square_size//2)
            pygame.draw.line(screen,color,start_pos,end_pos,1)

class Game:
    def __init__(self,caption) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([screen_w,screen_h])
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock()

        self.is_play = False

        self.map = Map(web_broad,web_broad)
        self.player = MAP_ENUM.player1
        self.winner = None

    def start(self):
        self.is_play = True
        self.player = MAP_ENUM.player1
        self.map.get_init()

    def play(self):
        # 画底板
        self.clock.tick(60)
        wood_color = (210,180,140)
        pygame.draw.rect(self.screen,wood_color,pygame.Rect(0,0,map_w,screen_h))
        pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(map_w,0,info_w,screen_h))


if __name__ == "__main__":
    while True:
     Game('五子棋').play()
     Map(750,750)