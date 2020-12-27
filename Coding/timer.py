import pygame
from setting import *

pygame.init()

screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font("./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf", 20)

def timer():
    now = 0
    minutes = 20
    seconds = 00
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 使用者按關閉鈕
                running = False

        if minutes < 10:
            if seconds < 10:
                remain_time = '0' + str(minutes) + ':' + '0' + str(seconds)
            else:
                remain_time = '0' + str(minutes) + ':' + str(seconds)
        else:
            remain_time = str(minutes) + ':' + str(seconds)

        time = pygame.time.get_ticks() / 1000
        int_time = int(time)
        if now != int_time:
            seconds -= 1
            now = int_time
            remain_time_word = font.render('Remaining Time = ' + remain_time, True, (255,255,255), (0,0,0))
            screen.blit(remain_time_word, (WIDTH - remain_time_word.get_width() - 10,0))
            pygame.display.update()

        if seconds <= 0 and minutes != 0:
            seconds = 59
            minutes -= 1
        elif seconds < 0 and minutes == 0:
            running = False
