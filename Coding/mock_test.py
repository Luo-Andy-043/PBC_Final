if __name__ == '__main__':
    import pygame, os

    # 修正程式作業位置
    working_path = os.path.dirname(__file__)
    os.chdir(working_path)

    # 啟動pygame
    pygame.init()

    # 建立視窗
    screen = pygame.display.set_mode((1120,630))
    pygame.display.set_caption('Game')
    screen.fill((255,255,255))

class little_game:
    
    def mock_test(self):
        # 載入寫考卷圖片
        pic0 = pygame.image.load('./素材/考卷/0.png')
        pic1 = pygame.image.load('./素材/考卷/1.png')
        pic2 = pygame.image.load('./素材/考卷/2.png')
        pic3 = pygame.image.load('./素材/考卷/3.png')
        pic4 = pygame.image.load('./素材/考卷/4.png')
        pic5 = pygame.image.load('./素材/考卷/5.png')
        end = pygame.image.load('./素材/考卷/gameover.png')
        win = pygame.image.load('./素材/考卷/win.png')
        test = [pic0, pic1, pic2, pic3, pic4, pic5]
        # MainLoop
        run = True
        hit = 0
        i = 3  # 開始的時候是三層
        add = 0
        while run:
            pygame.time.delay(100)
            # clock.tick(30)
            if __name__ == '__main__':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

            if 1 <= i <= 5:
                # 每隔一段時間增加一層
                add += 1
                if add == 11:
                    i += 1
                    add = 0

                # 敲幾下空白可以消一層
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_SPACE]:
                    hit += 1

                if hit >= 6:
                    i -= 1
                    hit = 0

                # 如果還沒到頂就再往上
                if 0 < i <= 5:
                    test[i] = pygame.transform.smoothscale(test[i], (1120,630))
                    screen.blit(test[i], (0,0))
                    pygame.display.update()

            # 到頂ㄌ就掰掰
            elif i > 5:
                end = pygame.transform.smoothscale(end, (1120,630))
                screen.blit(end, (0,0))
                pygame.display.update()

            # 寫完就贏ㄌ 耶
            else:
                win = pygame.transform.smoothscale(win, (1120,630))
                screen.blit(win, (0,0))
                pygame.display.update()
    
    def egg_game(self):
        move_egg = False
        move_ok_egg = False
        egg_pos = 0, 0
        okegg_pos = 290, 445
        egg_appear = False
        raw_egg_appear = False
        ok_egg_appear = False
        cook = 0
        wait = 0
        eaten = 0
        run = True
        # 載入圖片
        kitchen = pygame.image.load('./素材/煎蛋/新廚房.png')
        egg = pygame.image.load('./素材/煎蛋/生蛋.png')
        raw_egg = pygame.image.load('./素材/煎蛋/生荷包蛋.png')
        ok_egg = pygame.image.load('./素材/煎蛋/熟荷包蛋.png')
        win = pygame.image.load('./素材/考卷/win.png')
        
        # 載入音效
        swallow = pygame.mixer.Sound('./素材/煎蛋/吞.mp3')
        swallow.set_volume(0.2)
        fry = pygame.mixer.Sound('./素材/煎蛋/煎蛋.mp3')
        fry.set_volume(0.2)
        
        # 載入字
        fontobj = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 64)

        while run:
            # 畫廚房背景
            kitchen = pygame.transform.smoothscale(kitchen, (1120, 630))
            screen.blit(kitchen, (0,0))
            
            # 顯示已吃幾顆
            textsurfaceobj = fontobj.render(str(eaten)+'/5', True, (0,0,0), (255,255,255))
            textrectobj = textsurfaceobj.get_rect()
            textrectobj.center = (970,100)
            screen.blit(textsurfaceobj, textrectobj)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                position = pygame.mouse.get_pos()
                # 如果在蛋區點一下就會出現一顆蛋
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 785 <= position[0] <= 974 and 327 <= position[1] <= 553 and raw_egg_appear == False and ok_egg_appear == False:
                        if event.button == 1:
                            egg_appear = True
                            egg_pos = position[0]-67.5, position[1]-50
                # 按住蛋/熟的蛋可以拖曳
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if egg_pos[0]-67.5 <= position[0] <= egg_pos[0]+67.5 and egg_pos[1]-50 <= position[1] <= egg_pos[1]+50:
                            move_egg = True
                        if ok_egg_appear == True and okegg_pos[0]-67.5 <= position[0] <= okegg_pos[0]+67.5 and okegg_pos[1]-50 <= position[1] <= okegg_pos[1]+50:
                            move_ok_egg = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        move_egg = False
                        move_ok_egg = False
            if move_egg:
                egg_pos = pygame.mouse.get_pos()

            if egg_appear:
                egg = pygame.transform.smoothscale(egg, (135, 100))
                screen.blit(egg, (egg_pos[0]-67.5, egg_pos[1]-50))
            
            # 如果打蛋拖到鍋子上放開 蛋就會變成生荷包蛋
            if 182 <= egg_pos[0] <= 412 and 336 <= egg_pos[1] <= 552 and move_egg == False:
                    egg_appear = False
                    raw_egg_appear = True
            
            # 計時煮了多久
            if raw_egg_appear:
                cook += 1
            
            # 煮一段時間之後生蛋就會變熟蛋
            if raw_egg_appear and cook <= 60: 
                raw_egg = pygame.transform.smoothscale(raw_egg, (135, 100))
                screen.blit(raw_egg, (230,400))
                fry.play()
            elif raw_egg_appear and cook > 60:
                ok_egg_appear = True
                okegg_pos = 290, 445
                fry.stop()
                
            # 熟了之後動蛋     
            if move_ok_egg:
                okegg_pos = pygame.mouse.get_pos()

            # 蛋進嘴巴
            if 449 <= okegg_pos[0] <= 668 and 173 <= okegg_pos[1] <= 242:
                ok_egg_appear = False
                raw_egg_appear = False
                eaten += 1
                swallow.play()
                # 回到最一開始ㄉ狀態
                move_egg = False
                move_ok_egg = False
                egg_pos = 0, 0
                okegg_pos = 290, 445
                egg_appear = False
                raw_egg_appear = False
                ok_egg_appear = False
                cook = 0
             
            # 蛋還沒進嘴巴
            if ok_egg_appear:
                ok_egg = pygame.transform.smoothscale(ok_egg, (135, 100))
                screen.blit(ok_egg, (okegg_pos[0]-67.5, okegg_pos[1]-50))
            
            #延遲一下再顯示贏ㄉ畫面
            if eaten == 5:
                wait += 1
            
            # 吃五顆蛋就過關
            if wait > 10:
                win = pygame.transform.smoothscale(win, (1120,630))
                screen.blit(win, (0,0))
            
            pygame.display.update()
    # def guess_song(self):
        

# 玩遊戲!
play = little_game()
play.egg_game()
pygame.quit()
