import pygame, os

# 路徑
game_path = os.path.dirname(__file__)
start_img_path = os.path.join(game_path, '遊戲開始_tmp_工作區域 1.png')
light_button_path = os.path.join(game_path, 'button_light.png')
dark_button_path = os.path.join(game_path, 'button_dark.png')

# 變數
screen_size = (960, 540)
start_button_length, start_button_height = 196, 115
start_button_x, start_button_y = 640, 270

# 啟動pygame
pygame.init()

# 建立視窗
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('管管大冒險')

# 載入「開始遊戲」圖片
start_img = pygame.image.load(start_img_path)
start_img.convert_alpha()
start_img = pygame.transform.smoothscale(start_img, screen_size)
screen.blit(start_img,(0,0))

# 載入「START」按鈕
light_button = pygame.image.load(light_button_path)
dark_button = pygame.image.load(dark_button_path)

start_button = dark_button  # 預設為正常顏色的按鈕
start_button.convert_alpha()
start_button = pygame.transform.smoothscale(start_button, (start_button_length, start_button_height))
screen.blit(start_button, (start_button_x, start_button_y))

# 更新
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
    hover = start_button_x <= mouse[0] <= start_button_x+start_button_length and \
            start_button_y <= mouse[1] <= start_button_y+start_button_height
    if hover:
        start_button = light_button
    else:
        start_button = dark_button

    start_button.convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (start_button_length,start_button_height))
    screen.blit(start_button, (start_button_x, start_button_y))
    pygame.display.update()

    # 按下按鈕會發生什麼事（目前先用關閉視窗取代）
    if hover and pygame.mouse.get_pressed()[0] is True:
        running = False

pygame.quit()
