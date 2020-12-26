import pygame, os
import opening

# 更正程式工作位置
working_path = os.path.dirname(__file__)
os.chdir(working_path)

# 路徑
start_img_path = './素材/start_game/遊戲開始.png'
light_button_path = './素材/start_game/button_light.png'
dark_button_path = './素材/start_game/button_dark.png'
start_guan_path_l = './素材/start_game/管管腳踏車（去背）_左.png'
start_guan_path_r = './素材/start_game/管管腳踏車（去背）_右.png'
menu_music_path = './素材/music/menu_music.wav'
game_music_path = './素材/music/game_music.mp3'

# 變數
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_size = (960, 540)
start_button_length, start_button_height = 159, 92
start_button_x, start_button_y = 550, 270

# 啟動pygame
pygame.init()
pygame.mixer.init()

# 建立視窗、畫布
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('管管大冒險')
bg = pygame.Surface(screen.get_size()).convert()
bg.fill(WHITE)

# 載入「開始遊戲」圖片、管管
start_img = pygame.image.load(start_img_path)
start_img.convert_alpha()
start_img = pygame.transform.smoothscale(start_img, screen_size)
GUAN_l = pygame.image.load(start_guan_path_l).convert_alpha()
GUAN_l = pygame.transform.smoothscale(GUAN_l, (414,234))
GUAN_r = pygame.image.load(start_guan_path_r).convert_alpha()
screen.blit(start_img,(0,0))
screen.blit(GUAN_l, (250, 300))

# 載入「START」按鈕
light_button = pygame.image.load(light_button_path)
dark_button = pygame.image.load(dark_button_path)
start_button = dark_button  # 預設為正常顏色的按鈕
start_button.convert_alpha()
start_button = pygame.transform.smoothscale(start_button, (start_button_length, start_button_height))
screen.blit(start_button, (start_button_x, start_button_y))

def fadeout(color = BLACK):
    '''淡出成全黑'''
    fadeout = pygame.Surface(screen_size).convert()
    fadeout.fill(color)
    for i in range(150):
        fadeout.set_alpha(i)
        screen.blit(fadeout, (0,0))
        pygame.display.update()
        pygame.time.delay(10)

# 更新
pygame.display.update()

'''遊戲開始'''
# MainLoop
clock = pygame.time.Clock()
running = True
quit_game = False

# 音樂
menu_music = pygame.mixer.music.load(menu_music_path)
# menu_music.pygame.mixer.music.set_volumn(0.5)
pygame.mixer.music.play(-1)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        # 使用者關閉視窗
        if event.type == pygame.QUIT:
            running = False
            quit_game = True

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

    # 按下按鈕，結束開啟頁面
    if hover and pygame.mouse.get_pressed()[0] is True:
        fadeout()
        running = False

'''進入地圖'''

class Player(pygame.sprite.Sprite):
    '''角色 Sprite'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(start_guan_path_l).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (192,108))
        # self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (480, 350)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        '''鍵盤操作'''
        accer = 0.08
        keystate = pygame.key.get_pressed()

        # 左鍵
        if keystate[pygame.K_LEFT]:
            self.speedx -= accer
            if self.speedx <= -6.5:
                self.speedx = -6.5
        if not keystate[pygame.K_LEFT] and self.speedx < 0:
            self.speedx += accer
            if self.speedx >= 0:
                self.speedx = 0

        # 右鍵
        if keystate[pygame.K_RIGHT]:
            self.speedx += accer
            if self.speedx >= 6.5:
                self.speedx = 6.5
        if not keystate[pygame.K_RIGHT] and self.speedx > 0:
            self.speedx -= accer
            if self.speedx <= 0:
                self.speedx = 0

        # 上鍵
        if keystate[pygame.K_UP]:
            self.speedy -= accer
            if self.speedy <= -6.5:
                self.speedy = -6.5
        if not keystate[pygame.K_UP] and self.speedy < 0:
            self.speedy += accer
            if self.speedy >= 0:
                self.speedy = 0

        # 下鍵
        if keystate[pygame.K_DOWN]:
            self.speedy += accer
            if self.speedy >= 6.5:
                self.speedy = 6.5
        if not keystate[pygame.K_DOWN] and self.speedy > 0:
            self.speedy -= accer
            if self.speedy <= 0:
                self.speedy = 0

        # 位移疊加速度
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # 方向向左/右，臉朝向左/右
        if self.speedx < 0:
            self.image = GUAN_l
        elif self.speedx > 0:
            self.image = GUAN_r
        elif self.speedx == 0:
            self.image = self.image


# Opening
opening.opening()
fadeout()
pygame.mixer.music.stop()
pygame.mixer.music.unload()

# 精靈設定
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
GUAN_r = pygame.transform.smoothscale(GUAN_r, (192,108))
GUAN_l = pygame.transform.smoothscale(GUAN_l, (192,108))

# MainLoop
running = True

# 音樂
game_music = pygame.mixer.music.load(game_music_path)
# game_music.pygame.mixer.music.set_volumn(0.5)
pygame.mixer.music.play(-1)

while running and quit_game is False:
    clock.tick(60)

    for event in pygame.event.get():
        # 使用者關閉視窗
        if event.type == pygame.QUIT:
            running = False

    # 載入地圖
    screen.blit(bg, (0,0))

    # Sprites
    # Update
    all_sprites.update()

    # Draw
    all_sprites.draw(screen)

    # 畫布更新
    pygame.display.update()

pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()
