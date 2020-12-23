# 使用開始遊戲圖片測試對話框視窗
import pygame

# 啟動pygame
pygame.init()

# 建立視窗
screen_size = (960, 540)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('管管大冒險')


# 載入「開始遊戲」圖片
background = pygame.Surface(screen.get_size())
background.convert()
background.fill((0,0,0,30))
screen.blit(background,(0,0))


# 建立 Class 對話框
class DialogBox:

    # 載入對話框與頭像背景
    box_img = pygame.image.load('./素材/dialog_box/box.png')
    box_img = pygame.transform.smoothscale(box_img, (500,160))
    box_img.convert_alpha()

    head_background = pygame.image.load('./素材/dialog_box/head_background.png')
    head_background = pygame.transform.smoothscale(head_background, (157, 200))
    head_background.convert_alpha()

    # 載入字體
    font = pygame.font.Font("./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf", 28)


    # 初始化屬性
    def __init__(self, person_head, person_name, text):
        self.person_head = './素材/dialog_box/head/' + person_head + '.png' # 頭像路徑
        self.person_name = person_name  # 名稱
        self.text = text                # 要顯示的話，應該要是一個list



    def show_box(self):  # 顯示對話框的method

        """
        # 放慢更新頻率，準備字的效果
        clock.tick(1)
        """
        # 擷取螢幕，準備變暗
        #screen_transparent = screen.convert_alpha()

        # 把對話框跟頭貼上去，位置測試！
        self.person_head = pygame.image.load(self.person_head) # 讀取頭像
        self.person_head.convert_alpha()
        self.person_head = pygame.transform.smoothscale(self.person_head, (146,170))
        screen.blit(self.head_background, (20,290))
        screen.blit(self.person_head, (40,340))


        # 把XX說貼上去，位置測試！

        self.person_name = self.person_name + "說："
        self.person_name = self.font.render(self.person_name, True, (255,255,255))
        screen.blit(self.person_name, (70,490))


        # 把box貼上去，位置測試！
        screen.blit(self.box_img, (210,365))

    def show_text(self):
        # 顯示文字
        for aSentence in self.text:
            sentence = self.font.render(aSentence, True, (131,31,40))
            screen.blit(sentence, (260,400))
            if pygame.mouse.get_pressed()[0]:
                break


        """
        while True:
            for i in range(len(self.text)):
                i = i.split()

            for i in range(len(self.text)):
                for j in i

            # 恢復正常
            clock.tick(60)
        """





# 建立開始的「管管對話框」物件實驗看看
guanguan_start = DialogBox("guanguan", "管管", ["原來...", "你就是台大生嗎...."])

guanguan_start.show_box()
guanguan_start.show_text()



# 設定計時器、刷新螢幕的迴圈
clock = pygame.time.Clock()
running = True


while running:
    clock.tick(60)

    for event in pygame.event.get():
        # 使用者關閉視窗
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()
