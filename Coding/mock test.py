import pygame
pygame.init()
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption('Mock test')
screen.fill((255,255,255))

pic0 = pygame.image.load('./素材/考卷/0.png')
pic1 = pygame.image.load('./素材/考卷/1.png')
pic2 = pygame.image.load('./素材/考卷/2.png')
pic3 = pygame.image.load('./素材/考卷/3.png')
pic4 = pygame.image.load('./素材/考卷/4.png')
pic5 = pygame.image.load('./素材/考卷/5.png')
end = pygame.image.load('./素材/考卷/gameover.png')
win = pygame.image.load('./素材/考卷/win.png')


test = [pic0, pic1, pic2, pic3, pic4, pic5]

run = True
hit = 0
i = 3  # 開始的時候是三層
add = 0
while run:
    pygame.time.delay(100)
    # clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if 1 <= i <= 5:
        # 每隔一段時間增加一層
        add += 1
        if add == 10:
            i += 1
            add = 0
        
        # 敲幾下空白可以消一層
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            hit += 1
        
        if hit == 7:
            i -= 1
            hit = 0
        
        # 如果還沒到頂就再往上
        if 0 < i <= 5:
            test[i] = pygame.transform.smoothscale(test[i], (960, 540))
            screen.blit(test[i], (0,0))
            pygame.display.update()
    # 到頂ㄌ就掰掰
    elif i > 5:
        end = pygame.transform.smoothscale(end, (960,540))
        screen.blit(end, (0,0))
        pygame.display.update()
    # 寫完就贏ㄌ 耶
    else:
        win = pygame.transform.smoothscale(win, (960,540))
        screen.blit(win, (0,0))
        pygame.display.update()

pygame.quit()
    