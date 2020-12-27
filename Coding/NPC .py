'''
分三部分：
1 在GLOBAL增加的變數與函數
2 程式部分
3 指派object
'''



'''1 在GLOBAL增加的變數與函數'''
# 破關變數與函數
schedule = int(0)
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
    def __init__(self, code, dbt_path, lbt_path, place, size=(110, 160)):
       self.code = code #A或B
        # 設定圖片路徑
        dbt_path = './素材/button/' + dbt_path + 'png'
        self.dbt_path = dbt_path
        lbt_path = './素材/button/' + lbt_path + 'png'
        self.lbt)path = lbt_path
        # 尺寸、位置
        self.size = size        
        self.place = place
        # 使用函數放出圖片
        self.dbt = img(self.dbt_path, size)
        self.lbt = img(self.lbt_path, size)

        
    def show(self):
        self.normalbt = self.dbt  # 預設為正常顏色的按鈕
        screen.blit(normalbt, self.place)
        # 游標在按鈕上時變色
        mouse = pygame.mouse.get_pos()
        hover = start_button_x <= mouse[0] <= start_button_x+start_button_length and \
                start_button_y <= mouse[1] <= start_button_y+start_button_height
        if hover:
            nomalbt = lbt
        else:
            normalbt = dbt
        pygame.display.update()

        if hover and pygame.mouse.get_pressed()[0] is True:
            global chosen
            chosen = self.code
 
  
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
def text(path)
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
'''
# 合併繪製_mode2
def dialog_NPC(name, imgpath, txtpath, select_mode = False):
    # 預設沒有選項按鈕

    # 如果有選項按鈕
    if select_mode is True:
        screen.blit(select_button_A, (720, 365))  # 左按鈕
        screen.blit(select_button_B, (840, 365))  # 右按鈕
    pic_speaker(name, imgpath) # 在NPC中，就是self.name,self.imgpath
    text(txtpath) # 在NPC中，是self.txt

# 型三：管管自說自話
def dialog_Guan(txtpath):
    pic_speaker('管管', './素材/dialog_box/head/管管.png') 
    text(txtpath)
'''
# 合併型(測試中)
def dialog(txtpath, name = '管管', imgpath = './素材/dialog_box/head/管管.png'):
    # 如果是管管獨白，dialog(只需要輸入檔案路徑)
    # 如果是腳色獨白，dialog(txtpath, self.name, self.imgpath)
    pic_speaker(name, imgpath) # 在NPC中，就是self.name,self.path
    text(txtpath) # 在NPC中，是self.txt


'''2 程式部分'''
class NPC(pygame.sprite.Sprite):    
    # 初始
    def __init__(self, name, place, index, mode, size=(80,80)):
        # name: 腳色名字；place: 腳色座標；index: 腳色的關卡次序(第幾關)；mode: 說話模式
        self.name = name  # 正式名字
        self.place = place  # 座標
        self.index = index  # 關卡次序
        self.mode = list(mode)  # 說話模式
        self.size = size  # 圖片大小
        self.imgpath = './素材/NPCPic/' + self.name + '.png' #圖片路徑       
        self.img = img(self.imgpath, size)  # 用函數載圖片
        screen.blit(self.img, self.place)  # 畫出角色
    

    # 觸發
    def encounter(self):
        global schedule
        if pygame.sprite.collide_rect(self, guan):
            if schedule == self.index:  # 找對人了
                for i = range(len(self.mode)-1):  #moden兩種，三格[0,1,2]
                    way_to_talk = self.mode[i+1] # 讀進來的模式，第幾句話的講話方法
                    txtpath = './素材/NPCText/' + self.name + str(i) + '.txt'
                    if way_to_talk == 1:
                        script = txt(txtpath)
                        script[]
                        dialog()
                        chosen = 'notyet'
                        button_A = button('A', 'dSelBt_A', 'lSelBt_A', (720, 365))
                        button_B = button('B', 'dSelBt_B', 'lSelBt_A', (840, 365))
                        button_A.show()
                        button_B.show()

                        # 選不到對的或還沒選
                        while chosen != 'A':
                            if chosen = 'B':
                                replypath = './素材/NPCText/' + self.name + B + '.txt'
                                dialog(replypath, self.name, self.imgpath)
                                dialog(txtpath, self.name, self.imgpath)
                        
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