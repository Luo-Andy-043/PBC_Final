import pygame, os
from setting import *

# 更正程式工作位置
working_path = os.path.dirname(__file__)
working_path="/Users/yichinhuang/Desktop/PBC_Final/PBC_Final/Coding"
os.chdir(working_path)

# 啟動pygame
pygame.init()

# 路徑
bg1_path = './素材/opening/opening_bg_1.png'
bg2_path = './素材/opening/opening_bg_2.png'
bg3_path = './素材/opening/opening_bg_3.png'
bg4_path = './素材/opening/opening_bg_4.png'

# 建立視窗、畫布
screen = pygame.display.set_mode(screen_size)

# 載入圖片
bg1 = pygame.image.load(bg1_path).convert_alpha()
bg1 = pygame.transform.smoothscale(bg1, screen_size)
bg2 = pygame.image.load(bg2_path).convert_alpha()
bg2 = pygame.transform.smoothscale(bg2, screen_size)
bg3 = pygame.image.load(bg3_path).convert_alpha()
bg3 = pygame.transform.smoothscale(bg3, screen_size)
bg4 = pygame.image.load(bg4_path).convert_alpha()
bg4 = pygame.transform.smoothscale(bg4, screen_size)
switcher = [bg1, bg2, bg3, bg4]

def opening():
    '''描述故事情節'''
    # 畫上圖片
    screen.blit(bg1, (0,0))
    pygame.display.update()

    # 按下左鍵切換
    index = 0
    run = True
    while run:
        for event in pygame.event.get():
            # 使用者關閉視窗
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 按下左鍵
                    index += 1
                    if index == 4:
                        run = False
                    else:
                        to_show = switcher[index]
                        screen.blit(to_show, (0,0))
                        pygame.display.update()