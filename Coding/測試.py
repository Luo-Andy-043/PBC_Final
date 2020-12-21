'''
筆記/
座標是以左上角為原點，向右向下為正。
畫完物件後，需要更新畫布(pygame.display.update())，執行後畫布上才會顯示出來
載入圖片時不能畫畫布
字要寫在視窗內
字體：要使用路徑法


參考資料紀錄/
https://hackmd.io/@UltraGeek/ryuS9iyy8?type=view
'''
import pygame

# 啟動Pygame
pygame.init()

# 建立「視窗」
screen = pygame.display.set_mode((1280, 720))
# 視窗標題
pygame.display.set_caption("基本架構")

# 建立「畫布」
# screen.get_size(): 取得視窗大小
# 畫布.convert(): 加快運行
background = pygame.Surface(screen.get_size())
background = background.convert()

# 設定畫布顏色(R,G,B)
background.fill((255,255,255))

# 在「視窗」上畫上「畫布」, (0,0): 繪製位置
screen.blit(background, (0,0))

# 寫字
# 字體變數
# aFont = pygame.font.Font('C:\\Users\\元G\\Desktop\\wts47.ttf', 40)
# 文字變數
# word = aFont.render('中文', 1, (100,21,194), (255,255,255))
# screen.blit(word, (320-word.get_width()//2, 160-word.get_height()//2))  # 置中


# 載入圖片
button = pygame.image.load('C:\\Users\\元G\\Desktop\\商管程式設計\\Final_Project\\素材\\畫作\\button_dark.png')
button.convert_alpha()
button = pygame.transform.smoothscale(button, (230,109))
screen.blit(button, (525,310))

pygame.display.update()

# 音效物件
# effect = pygame.mixer.Sound('C:\\Users\\元G\\Downloads\\sound.wav')
# effect.set_volume(0.5)  # 0.0~1.0
# effect.play()

# 音樂物件
# sound = pygame.mixer.music.load('C:\\Users\\元G\\Desktop\\music.mp3')
# pygame.mixer.music.play()

# 使用無窮迴圈，偵測使用者是否按下視窗關閉鍵，按下時結束程式
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 使用者按關閉鈕
            running = False

    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade
    if 525 <= mouse[0] <= 525+230 and 109 <= mouse[1] <= 109+310: 
        button = pygame.image.load('C:\\Users\\元G\\Desktop\\商管程式設計\\Final_Project\\素材\\畫作\\button_light.png')
    else:
        button = pygame.image.load('C:\\Users\\元G\\Desktop\\商管程式設計\\Final_Project\\素材\\畫作\\button_dark.png')
    button.convert_alpha()
    button = pygame.transform.smoothscale(button, (230,109))
    screen.blit(button, (525,310))
    pygame.display.update()

pygame.quit() # 關閉繪圖視窗
