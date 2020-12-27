import pygame, os
import opening
from setting import *
from map import *

# 更正程式工作位置
working_path = os.path.dirname(__file__)
os.chdir(working_path)

start_guan_path_l = './素材/start_game/管管腳踏車（去背）_左.png'
start_guan_path_r = './素材/start_game/管管腳踏車（去背）_右.png'

# 上、下、左、右
map_x, map_y = 0, 0

class Game:
    def __init__(self):
        #  initialize
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(TITLE)

        self.playing = True
        self.fail = False
        self.walls = pygame.sprite.Group()
        self.map = Map('./background.txt')
        self.camera = Camera(self.map.width, self.map.height)
        self.all_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.background = pygame.image.load('../視覺設計/地圖全圖_完稿_全.jpg').convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, (2700, 4500))

    def load(self):
        # all the paths
        self.start_img_path = './素材/start_game/遊戲開始.png'
        self.light_button_path = './素材/start_game/button_light.png'
        self.dark_button_path = './素材/start_game/button_dark.png'
        self.menu_music_path = './素材/music/menu_music.wav'
        self.game_music_path = './素材/music/game_music.mp3'
        self.reminder_6_path = './素材/reminder/reminder_6.png'
        self.reminder_5_path = './素材/reminder/reminder_5.png'
        self.reminder_4_path = './素材/reminder/reminder_4.png'
        self.reminder_3_path = './素材/reminder/reminder_3.png'
        self.reminder_2_path = './素材/reminder/reminder_2.png'
        self.reminder_1_path = './素材/reminder/reminder_1.png'
        self.reminder_30_path = './素材/reminder/reminder_30.png'
        self.reminder_10_path = './素材/reminder/reminder_10.png'
        self.reminder_times_up_path = './素材/reminder/times_up.png'
        # self.gameover_path = ''
        # self.close_game_path = ''
        

        # load images/music
        self.start_img = pygame.image.load(self.start_img_path).convert_alpha()
        self.start_img = pygame.transform.smoothscale(self.start_img, screen_size)

        self.GUAN_start = pygame.image.load(start_guan_path_l).convert_alpha()
        self.GUAN_start = pygame.transform.smoothscale(self.GUAN_start, (414,234))

        self.light_button = pygame.image.load(self.light_button_path)
        self.dark_button = pygame.image.load(self.dark_button_path)
        self.start_button = self.dark_button.convert_alpha()  # 預設為正常顏色的按鈕
        self.start_button = pygame.transform.smoothscale(self.start_button, (start_button_length, start_button_height))

        self.reminder_6 = pygame.image.load(self.reminder_6_path).convert_alpha()
        self.reminder_6 = pygame.transform.smoothscale(self.reminder_6, (513, 143))
        self.reminder_5 = pygame.image.load(self.reminder_5_path).convert_alpha()
        self.reminder_5 = pygame.transform.smoothscale(self.reminder_5, (513, 143))
        self.reminder_4 = pygame.image.load(self.reminder_4_path).convert_alpha()
        self.reminder_4 = pygame.transform.smoothscale(self.reminder_4, (513, 143))
        self.reminder_3 = pygame.image.load(self.reminder_3_path).convert_alpha()
        self.reminder_3 = pygame.transform.smoothscale(self.reminder_3, (513, 143))
        self.reminder_2 = pygame.image.load(self.reminder_2_path).convert_alpha()
        self.reminder_2 = pygame.transform.smoothscale(self.reminder_2, (513, 143))
        self.reminder_1 = pygame.image.load(self.reminder_1_path).convert_alpha()
        self.reminder_1 = pygame.transform.smoothscale(self.reminder_1, (513, 143))
        self.reminder_30 = pygame.image.load(self.reminder_30_path).convert_alpha()
        self.reminder_30 = pygame.transform.smoothscale(self.reminder_30, (513, 143))
        self.reminder_10 = pygame.image.load(self.reminder_10_path).convert_alpha()
        self.reminder_10 = pygame.transform.smoothscale(self.reminder_10, (513, 143))
        self.reminder_times_up = pygame.image.load(self.reminder_times_up_path).convert_alpha()
        self.reminder_times_up = pygame.transform.smoothscale(self.reminder_times_up, (513, 143))
        # self.gameover_img = pygame.image.load(self.gameover_path).convert_alpha()
        # self.gameover_img = pygame.transform.smoothscale(self.gameover_img, ())
        # self.close_game_img = pygame.image.load(self.close_game_path).convert_alpha()
        # self.close_game_img = pygame.transform.smoothscale(self.close_game_img, ())

    def new(self):
        # start a new game
        self.guan = GUAN(self, 92, 208)
        self.walls = pygame.sprite.Group()
        self.all_sprites.add(self.guan)
        self.bg = bg_class(self)
        self.load()
        self.show_start_game()
        opening.opening()
        self.wall_list = []
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    w = Wall(self, col, row)
                    self.wall_list.append(w)
        self.camera = Camera(self.map.width, self.map.height)
        self.music_stop()
        self.run()

    def watcher(self):
        self.time_past = (self.timer - self.start) / 1000
        if 0.5 <= self.time_past <= 1:
            self.screen.blit(self.reminder_6, (WIDTH/2-self.reminder_6.get_width()/2, HEIGHT/2-self.reminder_6.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
        if 61 <= self.time_past <= 61.5:
            self.screen.blit(self.reminder_5, (WIDTH/2-self.reminder_5.get_width()/2, HEIGHT/2-self.reminder_5.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
        if 120 <= self.time_past <= 120.5:
            self.screen.blit(self.reminder_4, (WIDTH/2-self.reminder_4.get_width()/2, HEIGHT/2-self.reminder_4.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
        if 180 <= self.time_past <= 180.5:
            self.screen.blit(self.reminder_3, (WIDTH/2-self.reminder_3.get_width()/2, HEIGHT/2-self.reminder_3.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
        if 240 <= self.time_past <= 240.5:
            self.screen.blit(self.reminder_2, (WIDTH/2-self.reminder_2.get_width()/2, HEIGHT/2-self.reminder_2.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
        if 300 <= self.time_past <= 300.5:
            self.screen.blit(self.reminder_1, (WIDTH/2-self.reminder_1.get_width()/2, HEIGHT/2-self.reminder_1.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
        if 330 <= self.time_past <= 330.5:
            self.screen.blit(self.reminder_30, (WIDTH/2-self.reminder_30.get_width()/2, HEIGHT/2-self.reminder_30.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
        if 350 <= self.time_past <= 350.5:
            self.screen.blit(self.reminder_10, (WIDTH/2-self.reminder_10.get_width()/2, HEIGHT/2-self.reminder_10.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
        if 360 <= self.time_past <= 360.5:
            self.screen.blit(self.reminder_times_up, (WIDTH/2-self.reminder_times_up.get_width()/2, HEIGHT/2-self.reminder_times_up.get_height()/2))
            pygame.display.update()
            pygame.time.delay(100)
            self.fail = True
    '''
    def fail(self):
        self.fail_img_path = ''
        self.fail_img = pygame.image.load(self.fail_img_path).convert_alpha()
        self.fail_img = pygame.transform.smoothscale(self.fail_img, ())
    '''

    def run(self):
        # Game Loop
        self.game_music = pygame.mixer.music.load(self.game_music_path)
        pygame.mixer.music.play(-1)

        # Timer
        self.start = pygame.time.get_ticks()
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(60) / 1000
            self.timer = pygame.time.get_ticks()
            self.watcher()
            self.draw_grid()
            self.events()
            # self.all_sprites.draw(self.screen)
            # for sprite in self.all_sprites:
                # self.screen.blit(sprite.image, self.camera.apply(sprite))
            self.screen.blit(self.bg.image, self.camera.apply(self.bg))
            self.screen.blit(self.guan.image, self.camera.apply(self.guan))
            for w in self.wall_list:
                self.screen.blit(w.image, self.camera.apply(w))
            # if self.fail == True:
                # self.gameover()
            self.update()
        self.music_stop()

    def events(self):
        # Game Loop - events
        self.L_click = False
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.L_click = True

    def music_stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def update(self):
        # Game Loop - Update
        pygame.display.update()
        self.all_sprites.update()
        self.camera.update(self.guan)

    def draw_grid(self):
        # draw the grids on the map
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def show_start_game(self):
        # the game starting screen
        self.load()
        self.playing = True
        self.screen.blit(self.start_img,(0,0))
        self.screen.blit(self.GUAN_start, (250, 300))
        self.screen.blit(self.start_button, (start_button_x, start_button_y))
        self.menu_music = pygame.mixer.music.load(self.menu_music_path)
        pygame.mixer.music.play(-1)

        while self.playing:
            self.events()

            self.mouse = pygame.mouse.get_pos()
            self.hover = start_button_x <= self.mouse[0] <= start_button_x+start_button_length and \
            start_button_y <= self.mouse[1] <= start_button_y+start_button_height

            if self.hover:
                self.start_button = self.light_button.convert_alpha()
            else:
                self.start_button = self.dark_button.convert_alpha()
                self.start_button.convert_alpha()
            self.start_button = pygame.transform.smoothscale(self.start_button, (start_button_length,start_button_height))
            self.screen.blit(self.start_button, (start_button_x, start_button_y))

            pygame.display.update()

            if self.hover and self.L_click:
                self.playing = False

    # def gameover(self):
        # screen.blit(self.gameover_img, (0,0))
        # self.update()
        # while True:
            # self.event()
            # if self.L_click:
                # self.playing = False
                # break

    # def close_game(self):
        # screen.blit(self.close_game_img, (0,0))
        # self.update()
        # while True:
            # self.event()
            # if self.L_click:
                # self.playing = False
                # break

class GUAN(pygame.sprite.Sprite):
    '''角色 Sprite'''
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        # self.GUAN_l = pygame.image.load(start_guan_path_l).convert_alpha()
        # self.GUAN_l = pygame.transform.smoothscale(self.GUAN_l, (60,60))
        # self.GUAN_r = pygame.image.load(start_guan_path_r).convert_alpha()
        # self.GUAN_r = pygame.transform.smoothscale(self.GUAN_r, (60,60))
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx = -sprite_speed
        if keys[pygame.K_RIGHT]:
            self.vx = sprite_speed
        if keys[pygame.K_UP]:
            self.vy = -sprite_speed
        if keys[pygame.K_DOWN]:
            self.vy = sprite_speed
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.707
            self.vy *= 0.707

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

    def collide_with_walls(self, d):
        if d == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x

        if d == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.set_alpha(100)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class bg_class(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.background
        self.rect = self.image.get_rect()
        


# Run the game
Guans_friend = Game()
Guans_friend.new()
pygame.quit()
