import pygame, os

# 更正程式工作位置
working_path = os.path.dirname(__file__)
os.chdir(working_path)

def opening():
    '''描述故事情節'''
    # 啟動pygame
    pygame.init()

    # 路徑
    bg_path = './素材/opening/opening_bg.png'
    opening_text_path = './素材/opening/opening.txt'

    # 變數
    screen_size = (960, 540)

    # 建立視窗、畫布
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('管管大冒險')

    # 畫上圖片
    opening_bg = pygame.image.load(bg_path).convert_alpha()
    opening_bg = pygame.transform.smoothscale(opening_bg, screen_size)
    screen.blit(opening_bg, (0, 0))
    pygame.display.update()
