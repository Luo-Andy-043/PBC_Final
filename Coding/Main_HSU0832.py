'''0｜IMPORT、環境路徑設置、通用函數集'''
import pygame, os
import opening
from setting import *
from map import *



# 更正程式工作位置
working_path = os.path.dirname(__file__)
os.chdir(working_path)


# 載圖片函數
def img(path, size):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.smoothscale(image, size)
    return image


# 載文字檔函數
def txt(text_path):
    with open(text_path, 'r', encoding = 'utf-8') as text:
        text_file = text.readlines()
    return text_file


# 按鈕函數：羅
class button(pygame.sprite.Sprite):
    # lbt:light_button
    # dbt:dark_button
    def __init__(self, game, dbt_path, lbt_path, place, size=(110, 160)):
        # 照片
        self.dbt_path = dbt_path
        self.lbt_path = lbt_path
        self.dbt = img(self.dbt_path, size)
        self.lbt = img(self.lbt_path, size)
        # 尺寸、位置
        self.size = size
        self.place = place
        # 使用函數放出圖片
        self.game = game

    def show(self):
        #顯示按鈕（按鈕要放在迴圈裡）
        self.normalbt = self.dbt
        self.game.screen.blit(self.normalbt, self.place)
        # 游標在按鈕上時變色
        self.choose = False
        self.mouse = pygame.mouse.get_pos()
        self.hover = self.place[0] <= self.mouse[0] <= self.place[0]+self.size[0] and \
                     self.place[1] <= self.mouse[1] <= self.place[1]+self.size[1]

        if self.hover:
            self.normalbt = self.lbt
        else:
            self.normalbt = self.dbt
        self.game.screen.blit(self.normalbt, self.place)
        pygame.display.update()

        if self.hover and self.game.L_click:
            self.choose = True
        return self.choose


# 按鈕函數：許
class buttonHSU(pygame.sprite.Sprite):
    # lbt:light_button
    # dbt:dark_button
    def __init__(self, game, dbt_path, lbt_path, place, size=(110, 160)):
        self.game = game
        # 設定圖片路徑
        self.dbt_path = './素材/button/' + dbt_path + '.png'
        self.lbt_path = './素材/button/' + lbt_path + '.png'
        # 尺寸、位置
        self.size = size        
        self.place = place
        # 使用函數放出圖片
        print(self.dbt_path)
        self.dbt = img(self.dbt_path, size)
        self.lbt = img(self.lbt_path, size)

    def show(self):
        #顯示按鈕（按鈕要放在迴圈裡）
        self.normalbt = self.dbt
        self.game.screen.blit(self.normalbt, self.place)
        # 游標在按鈕上時變色
        self.choose = False
        self.mouse = pygame.mouse.get_pos()
        self.hover = self.place[0] <= self.mouse[0] <= self.place[0]+self.size[0] and \
                     self.place[1] <= self.mouse[1] <= self.place[1]+self.size[1]

        if self.hover:
            self.normalbt = self.lbt
        else:
            self.normalbt = self.dbt
        self.game.screen.blit(self.normalbt, self.place)
        pygame.display.update()

        if self.hover and self.game.L_click:
            self.choose = True
        return self.choose


# 紀錄破關進度
schedule = 1
def yrpass():
    global schedule 
    schedule += 1


# 位置紀錄
NPCcamera_place = [0,0,0,0,0,0]
GUANcamera_place = [0,0]

'''1｜圖片、字型、素材載入'''
# 共用圖片
box_img = img('./素材/dialog_box/box.png', (500,160))
head_background = img('./素材/dialog_box/head_background.png', (157, 300))
select_button_A =  img('./素材/dialog_box/select_button_A.png', (110, 160))
select_button_B =  img('./素材/dialog_box/select_button_B.png', (110, 160))
guan_path_l = '../視覺設計/管管騎ubike（左_方形）.png'
guan_path_r = '../視覺設計/管管騎ubike（右_方形）.png'
guan_path_u = '../視覺設計/管管騎ubike（背_方形）.png'
guan_path_d = '../視覺設計/管管騎ubike（正_方形）.png'

# 字型
font = pygame.font.Font("./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf", 28)

'''2｜NPC相關程式'''

'''2.1｜對話框'''
# 零件：顯示說話者圖片
def pic_speaker(game, charname, headpath):
    # 載圖
    global head_background
    # global box_img
    NPC_head = img(headpath, (146,170)) # 使用函數

    # 繪製
    game.screen.blit(head_background, (20,250))
    game.screen.blit(NPC_head, (40,340))

    # 把XX說貼上去
    name = charname + "說："
    name = font.render(name, True, (139,0,0))
    game.screen.blit(name, (70,490))

# 零件：顯示文字之獨白
def text(game, path):
    global box_img
    # 字數上限：16字
    # 將一句話拆分成list，顯示一個一個字的效果
    file = txt(path)
    for line in file:       # 每一句話
        # 以覆蓋方式刪除上一句
        game.screen.blit(box_img, (210,365))
        for word in range(len(line)):    # 每句話的每個字
            sentence = font.render(line[:word+1], True, BLACK)
            game.screen.blit(sentence, (250,425))
            pygame.display.update()
            pygame.time.delay(200)

            # 如果一句render完了
            if word == len(line)-1:
                waiting = True
                last_line = file[-1]
                while waiting:
                    game.events()
                    if game.L_click:
                        waiting = False
                    if line == last_line:
                        waiting = False

# 組裝零件一＆零件二
def dialog(game, txtpath, name = '管管', imgpath = './素材/dialog_box/head/guanguan.png'):
    # 如果是管管獨白，dialog(只需要輸入檔案路徑)
    # 如果是腳色獨白，dialog(txtpath, self.name, self.imgpath)
    pic_speaker(game, name, imgpath) # 在NPC中，就是self.name, self.path
    text(game, txtpath) # 在NPC中，是self.txt


'''2.2｜NPC'''
class NPC(pygame.sprite.Sprite):
    # 初始
    def __init__(self, game, name, index, mode, size=(80,80)):
        # name: 腳色名字；place: 腳色座標；index: 腳色的關卡次序(第幾關)；mode: 說話模式
        self.groups = game.all_sprites
        self.game = game      # 所屬遊戲
        self.name = name      # 正式名字，兩個字
        self.index = index    # 關卡次序
        self.indicator = index-1
        self.mode = mode      # 說話模式，是個list
        self.size = size      # 圖片大小
        # self.place = place
        self.imgpath = './素材/NPCPic/' + self.name + '.png' #圖片路徑       
        self.image = img(self.imgpath, size)  # 用函數載圖片
        self.rect = self.image.get_rect()
        self.touch = False
        self.cooler = 45
        # game.screen.blit(self.image, CLERK_Place)
        # pygame.display.update()

    # 觸發
    def encounter(self):
        global schedule
        # 碰撞了 而且 找對人
        # self.they_encounters = False
        # self.they_encounters = pygame.sprite.collide_rect_ratio( 0.95 )(self, self.game.guan)
        self.touch = False 
        if (abs(NPCcamera_place[self.indicator][0] - GUANcamera_place[0]) < 40 and \
            abs(NPCcamera_place[self.indicator][1] - GUANcamera_place[1]) < 40):
            print(self.name, '媽我在這裡')
            self.touch = True
        
        if self.touch == True :
            if self.cooler==0:
                print(schedule, self.index)
                print(self.name)
                pygame.display.update()
                if schedule == self.index:
                    for i in range(len(self.mode)):  # model三種，四格[2,1,3] len=3 i = 0,1,2
                        way_to_talk = self.mode[i]   # 讀進來的模式，第幾句話的講話方法
                        txtpath = './素材/NPCText/' + self.name + str(i+1) + '.txt'
                        print('i=', i, 'way=', way_to_talk)
                        if way_to_talk == 1:
                            print('i=', i, 'way=', way_to_talk, 'now1')

                            button_A = buttonHSU(self.game, 'dSelBt_A', 'lSelBt_A', (720, 365))
                            button_B = buttonHSU(self.game, 'dSelBt_B', 'lSelBt_B', (840, 365))
                            choose_A, choose_B = False, False
                            dialog(self.game, txtpath, self.name, self.imgpath)

                            while choose_A is False:
                                self.game.events()
                                choose_A = button_A.show()
                                choose_B = button_B.show()
                                pygame.display.update()
                                if choose_B:
                                    print('i=', i, 'way=', way_to_talk, 'nowwrong')
                                    replypath = './素材/NPCText/' + self.name + 'B' + '.txt'
                                    dialog(self.game, replypath, self.name, self.imgpath)
                                    dialog(self.game, txtpath, self.name, self.imgpath)
                                    choose_B = False
                            # 對了
                            print('i=', i, 'way=', way_to_talk, 'nowright')
                            replypath = './素材/NPCText/' + self.name + 'A' + '.txt'
                            dialog(self.game, replypath, self.name, self.imgpath)
                            yrpass()
                            pygame.time.delay(1500)
                            self. cooler = 60
                            self.game.update()
                            

                        # 第二種講話模式
                        if way_to_talk == 2:  # NPC說一段話
                            print('i=', i, 'way=', way_to_talk, 'now2')
                            dialog(self.game, txtpath, self.name, self.imgpath)
                            pygame.display.update()
                            self. cooler = 45

                        # 第三種講話模式
                        if way_to_talk == 3:  # 管管說一段話
                            print('i=', i, 'way=', way_to_talk, 'now3')
                            dialog(self.game, txtpath)
                            pygame.display.update()
                            self. cooler = 45

                # 罐頭台詞
                else:
                    txtpath = './素材/NPCText/' + self.name + '0' + '.txt'
                    dialog(self.game, txtpath, self.name, self.imgpath) 
                    pygame.display.update()
                    self.cooler = 45
            else:
                self.cooler -= 1



'''3｜管中閔'''
class GUAN(pygame.sprite.Sprite):
    '''角色 Sprite'''
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.GUAN_l = img(guan_path_l, (60,60))
        self.GUAN_r = img(guan_path_r, (60,60))
        self.GUAN_u = img(guan_path_u, (60,60))
        self.GUAN_d = img(guan_path_d, (60,60))
        self.image = self.GUAN_r
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx = -sprite_speed
            self.image = self.GUAN_l
        if keys[pygame.K_RIGHT]:
            self.vx = sprite_speed
            self.image = self.GUAN_r
        if keys[pygame.K_UP]:
            self.vy = -sprite_speed
            self.image = self.GUAN_u
        if keys[pygame.K_DOWN]:
            self.vy = sprite_speed
            self.image = self.GUAN_d
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


'''4｜牆壁與地圖'''
class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.set_alpha(0)
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


'''5｜主程式'''

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

    # 載入素材
    def load(self):
        # all the paths
        self.start_img_path = './素材/start_game/遊戲開始.png'
        self.light_button_path = './素材/button/button_light.png'
        self.dark_button_path = './素材/button/button_dark.png'
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
        self.start_img = img(self.start_img_path, screen_size)
        self.reminder_6 = img(self.reminder_6_path, (513, 143))
        self.reminder_5 = img(self.reminder_5_path, (513, 143))
        self.reminder_4 = img(self.reminder_4_path, (513, 143))
        self.reminder_3 = img(self.reminder_3_path, (513, 143))
        self.reminder_2 = img(self.reminder_2_path, (513, 143))
        self.reminder_1 = img(self.reminder_1_path, (513, 143))
        self.reminder_30 = img(self.reminder_30_path, (513, 143))
        self.reminder_10 = img(self.reminder_10_path, (513, 143))
        self.reminder_times_up = img(self.reminder_times_up_path, (513, 143))
        self.GUAN_start = img(guan_path_l, (220,220))
        self.light_button = img(self.light_button_path, (start_button_length, start_button_height))
        self.dark_button = img(self.dark_button_path, (start_button_length, start_button_height))

        # self.gameover_img = pygame.image.load(self.gameover_path).convert_alpha()
        # self.gameover_img = pygame.transform.smoothscale(self.gameover_img, ())
        # self.close_game_img = pygame.image.load(self.close_game_path).convert_alpha()
        # self.close_game_img = pygame.transform.smoothscale(self.close_game_img, ())


    # 遊戲起始畫面
    def show_start_game(self):
        # the game starting screen
        self.load()
        start_button = button(self, self.dark_button_path, self.light_button_path, (550, 270), (159, 92))
        self.playing = True
        self.screen.blit(self.start_img,(0,0))
        self.screen.blit(self.GUAN_start, (345, 310))

        self.menu_music = pygame.mixer.music.load(self.menu_music_path)
        pygame.mixer.music.play(-1)

        start_the_game = False
        while not start_the_game:
            self.events()
            start_the_game = start_button.show()
            pygame.display.update()

    # 進入主遊戲(地圖)
    def new(self):
        # start a new game
        # 角色
        self.guan = GUAN(self, 88, 168)

        # 牆壁
        self.walls = pygame.sprite.Group()
        self.all_sprites.add(self.guan)

        # 背景
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
        self.music_stop()
        self.run()
    
    # 時間監控程式
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

    # 遊戲運作
    def run(self):
        # Game Loop
        self.game_music = pygame.mixer.music.load(self.game_music_path)
        pygame.mixer.music.play(-1)
        
        # NPC定義
        self.NPC_CLERK = NPC(self, '店員', 1, mode=[2,1,3])
        self.NPC_JK = NPC(self, '屁孩', 2, [3,2,3,2,1])
        self.NPC_student = NPC(self, '學生', 3, [2,1])
        self.NPC_elder = NPC(self, '老人', 4, [2,1])
        self.NPC_e = NPC( self, '函數', 5, [3,2,1])
        self.NPC_shortfarmer = NPC(self, '北北', 6, [2,1])
        

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
            
            
            # 物件呈現：牆與地圖
            self.screen.blit(self.bg.image, self.camera.apply(self.bg))
            for w in self.wall_list:
                self.screen.blit(w.image, self.camera.apply(w))            

                        
            #物件呈現：ＮＰＣ
            NPCcamera_place[0] = (self.camera.apply(self.NPC_CLERK)[0]+1820, self.camera.apply(self.NPC_CLERK)[1]+3020)
            NPCcamera_place[1] = (self.camera.apply(self.NPC_JK)[0]+2020, self.camera.apply(self.NPC_JK)[1]+2960)
            NPCcamera_place[2] = (self.camera.apply(self.NPC_student)[0]+1740, self.camera.apply(self.NPC_student)[1]+1720)
            NPCcamera_place[3] = (self.camera.apply(self.NPC_elder)[0]+1060, self.camera.apply(self.NPC_elder)[1]+400)
            NPCcamera_place[4] = (self.camera.apply(self.NPC_e)[0]+2160, self.camera.apply(self.NPC_e)[1]+500)
            NPCcamera_place[5] = (self.camera.apply(self.NPC_shortfarmer)[0]+1880, self.camera.apply(self.NPC_shortfarmer)[1]+500)
            GUANcamera_place[0] = self.camera.apply(self.guan)[0]
            GUANcamera_place[1] = self.camera.apply(self.guan)[1]

            self.screen.blit(self.NPC_CLERK.image,NPCcamera_place[0])
            self.screen.blit(self.NPC_JK.image, NPCcamera_place[1])            
            self.screen.blit(self.NPC_student.image,  NPCcamera_place[2])
            self.screen.blit(self.NPC_elder.image, NPCcamera_place[3])
            self.screen.blit(self.NPC_e.image, NPCcamera_place[4])
            self.screen.blit(self.NPC_shortfarmer.image, NPCcamera_place[5])


            # 物件呈現：管
            self.screen.blit(self.guan.image, self.camera.apply(self.guan))

        
            # NPC偵測
            self.NPC_CLERK.encounter()
            self.NPC_JK.encounter()
            self.NPC_student.encounter()
            self.NPC_elder.encounter()
            self.NPC_e.encounter()
            self.NPC_shortfarmer.encounter()
            
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
                pygame.quit()
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
        
    def draw_grid(self):  # 障礙物設定
        # draw the grids on the map
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))
    


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




        

'''6｜執行'''
# Run the game
Guans_friend = Game()
Guans_friend.new()
pygame.quit()
