import pygame, os

# 啟動pygame
pygame.init()

# 更正程式工作位置
working_path = os.path.dirname(__file__)
os.chdir(working_path)

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

def opening():
    '''描述故事情節'''
    # 開啟檔案
    with open(opening_text_path, 'r', encoding = 'utf-8') as file:
        opening_text = file.readlines()

    # MainLoop
    running = True
    while running:
        for event in pygame.event.get():
            # 使用者關閉視窗
            if event.type == pygame.QUIT:
                running = False

            # 寫入文字
            index = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 按下左鍵
                    index += 1
                    if index >= 12:
                        index = 12

            for i in range(len(opening_text[index])):  # 每一個字
                if 

        pygame.display.update()

    pygame.quit()
