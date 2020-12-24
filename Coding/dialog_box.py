# 對話框視窗
import pygame, os

# 更正程式工作位置
working_path = os.path.dirname(__file__)
os.chdir(working_path)

# 啟動pygame
pygame.init()

# 變數
WHITE = (255,255,255)
BLACK = (0,0,0)

# 建立視窗
screen_size = (960, 540)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('管管大冒險')

# 載入「開始遊戲」圖片
background = pygame.Surface(screen.get_size())
background.convert()
background.fill((0,0,0,128))  # 最後的值：透明度
screen.blit(background,(0,0))

# 載入圖片
box_img = pygame.image.load('./素材/dialog_box/box.png').convert_alpha()
box_img = pygame.transform.smoothscale(box_img, (500,160))
head_background = pygame.image.load('./素材/dialog_box/head_background.png').convert_alpha()
head_background = pygame.transform.smoothscale(head_background, (157, 200))
select_button_A = pygame.image.load('./素材/dialog_box/select_button_A.png').convert_alpha()
select_button_A = pygame.transform.smoothscale(select_button_A, (110, 160))
select_button_B = pygame.image.load('./素材/dialog_box/select_button_B.png').convert_alpha()
select_button_B = pygame.transform.smoothscale(select_button_B, (110, 160))

# 載入字體
font = pygame.font.Font("./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf", 28)

class DialogBox():
    '''建立對話框class'''

    def __init__(self, person_head, person_name, text_path):
        '''初始化屬性'''
        self.person_head = './素材/dialog_box/head/' + person_head + '.png' # 頭像路徑
        self.person_name = person_name  # 名稱
        # 講話內容
        with open(text_path, 'r', encoding = 'utf-8') as text:
            self.text_file = text.readlines()
        self.box_img = box_img
        self.head_background = head_background

    def show_box(self):
        '''顯示對話框的method'''
        # 擷取螢幕，準備變暗
        # screen_transparent = screen.convert_alpha()

        # 把對話框跟頭貼上去
        self.person_head = pygame.image.load(self.person_head) # 讀取頭像
        self.person_head.convert_alpha()
        self.person_head = pygame.transform.smoothscale(self.person_head, (146,170))
        screen.blit(self.head_background, (20,290))
        screen.blit(self.person_head, (40,340))

        # 把XX說貼上去
        self.person_name = self.person_name + "說："
        self.person_name = font.render(self.person_name, True, WHITE)
        screen.blit(self.person_name, (70,490))

        # 把box貼上去
        screen.blit(self.box_img, (210,365))

    # 顯示文字
    def show_text(self):
        '''字數上限：16字'''
        # 將一句話拆分成list，顯示一個一個字的效果
        for aline in self.text_file:       # 每一句話
            '''以覆蓋方式刪除上一句'''
            screen.blit(self.box_img, (210,365))
            for j in range(len(aline)):    # 每句話的每個字
                sentence = font.render(aline[:j+1], True, BLACK)
                screen.blit(sentence, (250,425))
                pygame.display.update()
                pygame.time.delay(200)

                # 如果一句render完了
                if j == len(aline)-1:
                    waiting = True
                    last_line = self.text_file[-1]
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:  # 按下左鍵
                                    waiting = False
                        if aline == self.text_file[-1]:
                            waiting = False

    # 顯示整個對話框
    def show_dialog(self, select_mode = False):
        '''整合「畫出框框」跟「畫出文字」'''
        # 預設沒有選項按鈕
        self.select_mode = select_mode

        # 如果有選項按鈕
        if select_mode is True:
            screen.blit(select_button_A, (720, 365))  # 左按鈕
            screen.blit(select_button_B, (840, 365))  # 右按鈕

        self.show_box()
        self.show_text()


# 建立開始的「管管對話框」物件實驗看看
# guanguan_start = DialogBox("guanguan", "管管", 'C:\\Users\\元G\\Desktop\\guan_say.txt')
# guanguan_start.show_dialog()

# 設定計時器、刷新螢幕的迴圈
# running = True
# while running:
    # pygame.display.update()
    # for event in pygame.event.get():
        # 使用者關閉視窗
        # if event.type == pygame.QUIT:
            # running = False

# pygame.quit()
