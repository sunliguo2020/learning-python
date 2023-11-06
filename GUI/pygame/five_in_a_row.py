import pygame

pygame.init()
screen = pygame.display.set_mode((750,750))
# 棋盘落子信息
map = [0]*15
for i in range(15):
    map[i] = [0] *15

# 哪一方在落子
player = 1
winner = 0

running = True

def check(row,col):
    # 判断左右方向是否五子联线
    score = 1
    # 水平往左判断
    for i in range(4):
        if  map[row][col+i] == map[row][col+i+1]:
            score = score + 1
        else:
            break
    # 水平往右判断
    for i in range(4):
        if map[row][col-i] == map[row][col-i-1]:
            score = score + 1
        else:
            break
    if score == 5:
        return True
    
    # 竖直往下判断
    for i in range(4):
        if  map[row+i][col] == map[row+i+1][col]:
            score = score + 1
        else:
            break
    # 垂直往上判断
    for i in range(4):
        if map[row-i][col] == map[row-i-1][col]:
            score = score + 1
        else:
            break
    if score == 5:
        return True


    # 判断右斜上
    for i in range(4):
        if  map[row-i][col+i] == map[row-i-1][col+i+1]:
            score = score + 1
        else:
            break
    # 右斜下
    for i in range(4):
        if map[row+i][col+i] == map[row+i+1][col-i+1]:
            score = score + 1
        else:
            break
    if score == 5:
        return True
    
     # 判断左斜上
    for i in range(4):
        if  map[row-i][col-i] == map[row-i-1][col-i-1]:
            score = score + 1
        else:
            break
    # 左斜下
    for i in range(4):
        if map[row+i][col-i] == map[row+i+1][col-i-1]:
            score = score + 1
        else:
            break
    if score == 5:
        return True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            col = round((x-25)/50)
            row = round((y-25)/50)
            # 显示落子坐标
            print(f"{player}正在落子，位置：{col,row}")
            if map[row][col] == 0:

                map[row][col] = player

                # 检查是否有获胜方
                if check(row,col):
                    # print("有人赢了！")
                    winner = player
                else:
                    # 切换角色
                    if player == 1:
                        player = 2
                    else:
                        player = 1
            else:
                print('没看到已经有棋子了吗？')

    screen.fill('#ee9a49')

    # 横线
    for x in range(15):
        pygame.draw.line(screen,'#000000',[25+50*x,25],[25+50*x,725],2)
    # 竖线
    for y in range(15):
        pygame.draw.line(screen,'#000000',[25,25+50*y],[725,25+50*y],2)
    
    pygame.draw.circle(screen,'#000000',[25+50*7,25+50*7],8)

    x,y = pygame.mouse.get_pos()

    x = round((x - 25)/50)*50+25
    y = round((y - 25)/50)*50+25

    # 落子提示
    pygame.draw.rect(screen,'#ffffff',[x-25,y-25,50,50],2)
    
    # 落子  根据落子信息画图形
    for row in range(15):
        for col in range(15):
            if map[row][col] ==1: # 黑方
                pygame.draw.circle(screen,'#000000',[col*50+25,row*50+25],25)
            elif map[row][col] == 2: # 白方
                pygame.draw.circle(screen,'#FFFFFF',[col*50+25,row*50+25],25)
    
    pygame.display.update()

    if winner !=0:
        if winner == 1:
            text = 'Black win'
            color = (0,0,0)
        else:
            text='White Win'
            color = (255,255,255)
        font = pygame.font.SysFont('',70)
        text_serface = font.render(text,True,color)
        text_position = (100,100)

        screen.blit(text_serface,text_position)
        pygame.display.update()
        # pygame.time.wait(3000)

        # running = False


pygame.quit()