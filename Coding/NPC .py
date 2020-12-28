import pygame
'''
分三部分：
1 在GLOBAL增加的變數與函數
2 程式部分
3 指派object
'''



'''1 在GLOBAL增加的變數與函數'''
# 破關變數與函數
schedule = 0
def yrpass():
    global schedule 
    schedule += 1
  

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
  

# 按鈕家族
class button(pygame.sprite.Sprite):
    # lbt:light_button
    # dbt:dark_button
    def __init__(self, game, dbt_path, lbt_path, place, size=(110, 160)):
        # 照片
        self.dbt_path = dbt_path
        self.lbt_path = lbt_path
        # 尺寸、位置
        self.size = size
        self.place = place
        # 使用函數放出圖片
        self.game = game

        
    def show(self):
        '''要放在迴圈裡'''
        self.dbt = img(self.dbt_path, self.size)
        self.lbt = img(self.lbt_path, self.size)
        self.normalbt = self.dbt
        self.game.screen.blit(self.normalbt, self.place)
        # 游標在按鈕上時變色
        self.choosing = False
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
            self.choosing = True

        return self.choosing


# 共用圖片
box_img = img('./素材/dialog_box/box.png', (500,160))
head_background = img('./素材/dialog_box/head_background.png', (157, 200))
select_button_A =  img('./素材/dialog_box/select_button_A.png', (110, 160))
select_button_B =  img('./素材/dialog_box/select_button_B.png', (110, 160))


# 繪製對話框系列函數：
# 三種類型：型一 選項；型二 腳色自說自話；型三 管管自說自話
# 零件：顯示說話者圖片
def pic_speaker(charname, headpath):
    # 載圖
    global head_background
    # global box_img
    NPC_head = img(headpath, (146,170)) # 使用函數

    # 繪製
    screen.blit(head_background, (20,290))
    screen.blit(NPC_head, (40,340))

    # 把XX說貼上去
    name = charname + "說："
    name = font.render(name, True, WHITE)
    screen.blit(name, (70,490))


# 零件：顯示文字之獨白
def text(path):
    global box_img
    '''字數上限：16字'''
    # 將一句話拆分成list，顯示一個一個字的效果
    file = txt(path)
    for line in file:       # 每一句話
        '''以覆蓋方式刪除上一句'''
        screen.blit(box_img, (210,365))
        for word in range(len(line)):    # 每句話的每個字
            sentence = font.render(aline[:word+1], True, BLACK)
            screen.blit(sentence, (250,425))
            pygame.display.update()
            pygame.time.delay(200)

            # 如果一句render完了
            if j == len(line)-1:
                waiting = True
                last_line = file[-1]
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:  # 按下左鍵
                                waiting = False
                    if line == file[-1]:
                        waiting = False


# 組裝
# 合併型(測試中)
def dialog(txtpath, name = '管管', imgpath = './素材/dialog_box/head/管管.png'):
    # 如果是管管獨白，dialog(只需要輸入檔案路徑)
    # 如果是腳色獨白，dialog(txtpath, self.name, self.imgpath)
    pic_speaker(name, imgpath) # 在NPC中，就是self.name,self.path
    text(txtpath) # 在NPC中，是self.txt


'''2 程式部分'''
class NPC(pygame.sprite.Sprite):
    '''要放在迴圈裡'''
    # 初始
    def __init__(self, game, name, place, index, mode, size=(80,80)):
        # name: 腳色名字；place: 腳色座標；index: 腳色的關卡次序(第幾關)；mode: 說話模式
        self.game = game     # 所屬遊戲
        self.name = name     # 正式名字，兩個字
        self.place = place   # 座標
        self.index = index   # 關卡次序
        self.mode = mode     # 說話模式，是個list
        self.size = size     # 圖片大小
        self.imgpath = './素材/NPCPic/' + self.name + '.png' #圖片路徑       
        self.img = img(self.imgpath, size)  # 用函數載圖片
        game.screen.blit(self.img, self.place)  # 畫出角色

    # 觸發
    def encounter(self):
        global schedule
        # 碰撞了 而且 找對人
        if pygame.sprite.collide_rect(self, self.game.guan) and schedule == self.index:
            for i in range(len(self.mode)):  # moden兩種，三格[0,1,2]
                way_to_talk = self.mode[i]   # 讀進來的模式，第幾句話的講話方法
                txtpath = './素材/NPCText/' + self.name + str(i) + '.txt'
                if way_to_talk == 1:
                    chosen = 'notyet'
                    button_A = button(self.game, 'A', 'dSelBt_A', 'lSelBt_A', (720, 365))
                    button_B = button(self.game, 'B', 'dSelBt_B', 'lSelBt_A', (840, 365))
                    choose_A, choose_B = False, False
                    while choose_A is False and choose_B is False:
                        self.game.events()
                        choose_A = button_A.show()
                        choose_B = button_B.show()
                        pygame.display.update()

                    # 選到不對的或還沒選
                    # while chosen != 'A':
                        # if chosen == 'B':
                            # replypath = './素材/NPCText/' + self.name + B + '.txt'
                            # dialog(self.game, replypath, self.name, self.imgpath)
                            # dialog(self.game, txtpath, self.name, self.imgpath)
                    if choose_A is True and 
                    
                    # 對了
                    replypath = './素材/NPCText/' + self.name + A + '.txt'
                    dialog(replypath, self.name, self.imgpath)

                if way_to_talk == 2:  # NPC說一段話
                    # dialog_NPC(self.name, self.imgpath, txtpath)
                    dialog(txtpath, self.name, self.imgpath)
                
                if way_to_talk == 3:  #  管管說一段話
                    # dialog_Guan(txtpath)
                    dialog(txtpath)

            else:  # 罐頭台詞
               txtpath = './素材/NPCText/' + self.name + 0 + '.txt'
               dialog_NPC(self.name, self.image, txtpath) 


'''3 指派object'''
# NPC_clerk = NPC('店員', (150,150), 1, (2,1,3))

'''
NPC_JK = NPC('屁孩', place, 2, mode)
NPC_student = NPC('學生', place, 3, mode)
NPC_elder = NPC('老人', place, 4, mode)
NPC_e = NPC('e', place, 3, mode)
NPC_shortfarmer = NPC('學生', place, 3, mode)
'''




















