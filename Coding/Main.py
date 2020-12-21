import pygame

# 啟動pygame
pygame.init()

# 建立視窗
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('管管大冒險')

# 載入「開始遊戲」圖片
bg = pygame.image.load('C:\\Users\\元G\\Desktop\\GitHub_PBC\\PBC_Final\\Coding\\素材\\畫作\\遊戲開始_tmp_工作區域 1.png')
start_img = bg
start_img.convert_alpha()
start_img = pygame.transform.smoothscale(start_img, screen_size)
screen.blit(start_img,(0,0))

# 載入「START」按鈕
light_button = pygame.image.load('C:\\Users\\元G\\Desktop\\GitHub_PBC\\PBC_Final\\Coding\\素材\\畫作\\button_light.png')
dark_button = pygame.image.load('C:\\Users\\元G\\Desktop\\GitHub_PBC\\PBC_Final\\Coding\\素材\\畫作\\button_dark.png')

start_button = dark_button  # 預設為正常顏色的按鈕
start_button.convert_alpha()
start_button = pygame.transform.smoothscale(start_button, (196,115))
screen.blit(start_button, (768, 360))

pygame.display.update()

# MainLoop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        # 使用者關閉視窗
        if event.type == pygame.QUIT:
            running = False

    # 游標在按鈕上時變色
    mouse = pygame.mouse.get_pos()
    hover = 768 <= mouse[0] <= 768+196 and 360 <= mouse[1] <= 360+115
    if hover:
        start_button = light_button
    else:
        start_button = dark_button

    start_button.convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (196,115))
    screen.blit(start_button, (768, 360))
    pygame.display.update()

    # 按下按鈕會發生什麼事（目前先用關閉視窗取代）
    if hover and pygame.mouse.get_pressed()[0] is True:
        running = False

pygame.quit()
