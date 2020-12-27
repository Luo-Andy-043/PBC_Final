import random

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
        
        # 載入音效
        write = pygame.mixer.Sound('./素材/考卷/寫字.mp3')
        
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
                    write.play()

                if hit >= 6:
                    i -= 1
                    hit = 0

                # 如果還沒到頂就再往上
                if 0 < i <= 5:
                    test[i] = pygame.transform.smoothscale(test[i], (1120,630))
                    screen.blit(test[i], (0,0))
                    pygame.draw.rect(screen, (102,51,0), [60, 500, 1000, 40], 0)
                    pygame.draw.rect(screen, (102,51,0), [310, 540, 40, 70], 0)
                    pygame.draw.rect(screen, (102,51,0), [810, 540, 40, 70], 0)
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
        kitchen = pygame.image.load('./素材/煎蛋/背景.png')
        kitchen = pygame.transform.smoothscale(kitchen, (1120, 630))
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
        
        finish = False
        show = True
        while run:
            # 畫廚房背景
            screen.blit(kitchen, (0,0))
            
            # 顯示已吃幾顆
            score = fontobj.render(str(eaten)+'/5', True, (0,0,0), (255,255,255))
            screen.blit(score, (950,50))
            
            if eaten == 5:
                if show:
                    pygame.display.update()
                    show = False
                pygame.time.delay(1000)
                win = pygame.transform.smoothscale(win, (1120,630))
                screen.blit(win, (0,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                position = pygame.mouse.get_pos()
                # 如果在蛋區點一下就會出現一顆蛋
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 787 <= position[0] <= 1013 and 335 <= position[1] <= 558 and raw_egg_appear == False and ok_egg_appear == False:
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
            if 156 <= egg_pos[0] <= 392 and 312 <= egg_pos[1] <= 547 and move_egg == False:
                    egg_appear = False
                    raw_egg_appear = True
            
            # 計時煮了多久
            if raw_egg_appear:
                cook += 1
            
            # 煮一段時間之後生蛋就會變熟蛋
            if raw_egg_appear and cook <= 70: 
                raw_egg = pygame.transform.smoothscale(raw_egg, (135, 100))
                screen.blit(raw_egg, (210,380))
                fry.play()
            elif raw_egg_appear and cook > 70:
                ok_egg_appear = True
                okegg_pos = 275, 425
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
            
            pygame.display.update()
 
    def guess_song(self):
        
        # 載入圖片
        machine = pygame.image.load('./素材/猜歌/機器.png')
        wrong = pygame.image.load('./素材/猜歌/叉.png')
        wrong = pygame.transform.smoothscale(wrong, (100,100))
        right = pygame.image.load('./素材/猜歌/圈.png')
        right = pygame.transform.smoothscale(right, (100,100))
        
        # 載入音樂
        lowbou = pygame.mixer.Sound('./素材/猜歌/拔蘿蔔前奏.mp3')
        lowbou.set_volume(0.5)
        three = pygame.mixer.Sound('./素材/猜歌/三輪車前奏.mp3')
        three.set_volume(0.5)
        doggy = pygame.mixer.Sound('./素材/猜歌/哈巴狗前奏.mp3')
        doggy.set_volume(0.5)
        yes = pygame.mixer.Sound('./素材/猜歌/正確.mp3')
        yes.set_volume(0.5)
        no = pygame.mixer.Sound('./素材/猜歌/答錯.mp3')
        no.set_volume(1)
        
        # 字型
        fontobj = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 40)
        
        # 顏色
        normal = (102,51,0)
        light = (216,176,136)
        white = (255,255,255)
        
        Q1 = True
        Q2 = False
        Q3 = False
        option1 = False
        option2 = False
        option3 = False
        option4 = False
        # 以下編號為題號
        correct1 = False
        correct2 = False
        correct3 = False
        # 以下編號是位置
        wrong1 = False
        wrong2 = False
        wrong3 = False
        wrong4 = False
        # one2two = 0
        waito = 1500
        waitx = 300
        played = False
        done = False
        run = True
        while run:
            # 畫背景
            screen.fill((252,245,216))
            machine = pygame.transform.smoothscale(machine, (378,415))
            screen.blit(machine, (75,140))
            position = pygame.mouse.get_pos()
            win = pygame.image.load('./素材/考卷/win.png')
            
            # 每一題點四個選項出現圈或叉
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Q1:
                            if 75 <= position[0] <= 453 and 140 <= position[1] <= 555:
                                lowbou.stop()
                                lowbou.play()
                            if option1:
                                correct1 = True
                                lowbou.stop()
                            elif option2:
                                wrong2 = True
                                lowbou.stop()
                            elif option3:
                                wrong3 = True
                                lowbou.stop()
                            elif option4:
                                wrong4 = True
                                lowbou.stop()
                        if Q2:
                            if 75 <= position[0] <= 453 and 140 <= position[1] <= 555:
                                three.stop()
                                three.play()
                            if option1:
                                wrong1 = True
                                three.stop()
                            elif option2:
                                wrong2 = True
                                three.stop()
                            elif option3:
                                correct2 = True
                                three.stop()
                            elif option4:
                                wrong4 = True
                                three.stop()
                        if Q3:
                            if 75 <= position[0] <= 453 and 140 <= position[1] <= 555:
                                doggy.stop()
                                doggy.play()
                            if option1:
                                wrong1 = True
                                doggy.stop()
                            elif option2:
                                wrong2 = True
                                doggy.stop()
                            elif option3:
                                wrong3 = True
                                doggy.stop()
                            elif option4:
                                correct3 = True
                                doggy.stop()
            # 播音樂
            if Q1 and played == False:
                lowbou.play()
                played = True
            if Q2 and played == False:
                three.play()
                played = True
            if Q3 and played == False:
                doggy.play()
                played = True
            
            # 畫選項格子
            # option1
            if 470 <= position[0] <= 720 and 230 <= position[1] <= 313:
                pygame.draw.rect(screen, light, [470, 230, 250, 83], 0)
                option1 = True
            else:
                pygame.draw.rect(screen, normal, [470, 230, 250, 83], 0)
                option1 = False
            # option2
            if 770 <= position[0] <= 1020 and 230 <= position[1] <= 313:
                pygame.draw.rect(screen, light, [770, 230, 250, 83], 0)
                option2 = True
            else:
                pygame.draw.rect(screen, normal, [770, 230, 250, 83], 0)
                option2 = False
            # option3
            if 470 <= position[0] <= 720 and 343 <= position[1] <= 426:
                pygame.draw.rect(screen, light, [470, 343, 250, 83], 0)
                option3 = True
            else:
                pygame.draw.rect(screen, normal, [470, 343, 250, 83], 0)
                option3 = False
            # option4
            if 770 <= position[0] <= 1020 and 343 <= position[1] <= 426:
                pygame.draw.rect(screen, light, [770, 343, 250, 83], 0)
                option4 = True
            else:
                pygame.draw.rect(screen, normal, [770, 343, 250, 83], 0)
                option4 = False
            
            # 題目
            if Q1:
                answer11 = fontobj.render('拔蘿蔔', True, white)
                screen.blit(answer11,(540,240))
                answer12 = fontobj.render('火車快飛', True, white)
                screen.blit(answer12,(820,240))
                answer13 = fontobj.render('小星星', True, white)
                screen.blit(answer13,(540,353))
                answer14 = fontobj.render('小蜜蜂', True, white)
                screen.blit(answer14,(840,353))
            if Q2:
                answer11 = fontobj.render('捕魚歌', True, white)
                screen.blit(answer11,(540,240))
                answer12 = fontobj.render('兩隻老虎', True, white)
                screen.blit(answer12,(820,240))
                answer13 = fontobj.render('三輪車', True, white)
                screen.blit(answer13,(540,353))
                answer14 = fontobj.render('潑水歌', True, white)
                screen.blit(answer14,(840,353))
            if Q3:
                answer11 = fontobj.render('虎姑婆', True, white)
                screen.blit(answer11,(540,240))
                answer12 = fontobj.render('春神來了', True, white)
                screen.blit(answer12,(820,240))
                answer13 = fontobj.render('茉莉花', True, white)
                screen.blit(answer13,(540,353))
                answer14 = fontobj.render('哈巴狗', True, white)
                screen.blit(answer14,(840,353))
            
            # 點擊選項回應
            if correct1:
                yes.play()
                for i in range(waito):
                    screen.blit(right, (420,221))
                    pygame.display.update()
                correct1 = False
                Q1 = False
                Q2 = True
                played = False
            
            if correct2:
                yes.play()
                for i in range(waito):
                    screen.blit(right, (420,334))
                    pygame.display.update()
                correct2 = False
                Q2 = False
                Q3 = True
                played = False
            
            if correct3:
                yes.play()
                screen.blit(right, (720,334))
                pygame.display.update()
                pygame.time.delay(30000)
                correct3 = False
                done = True
            
            if done: # 三題都答完ㄌ
                win = pygame.transform.smoothscale(win, (1120,630))
                screen.blit(win, (0,0))
            
            if wrong1:
                no.play()
                for i in range(waitx):
                    screen.blit(wrong, (420,221))
                    pygame.display.update()
                wrong1 = False
            
            if wrong2:
                no.play()
                for i in range(waitx):
                    screen.blit(wrong, (720,221))
                    pygame.display.update()
                wrong2 = False
            
            if wrong3:
                no.play()
                for i in range(waitx):
                    screen.blit(wrong, (420,334))
                    pygame.display.update()
                wrong3 = False
            
            if wrong4:
                no.play()
                for i in range(waitx):
                    screen.blit(wrong, (720,334))
                    pygame.display.update()
                wrong4 = False
            
            pygame.display.update()
    
    def beatduck(self):
        size = (200,200)
        # 載入圖片
        bg = pygame.image.load('./素材/猜拳/背景.png')
        bg = pygame.transform.smoothscale(bg, (1120,630))
        paper = pygame.image.load('./素材/猜拳/布.png')
        paper = pygame.transform.smoothscale(paper, size)
        scissors = pygame.image.load('./素材/猜拳/剪刀.png')
        scissors = pygame.transform.smoothscale(scissors, size)
        stone = pygame.image.load('./素材/猜拳/石頭.png')
        stone = pygame.transform.smoothscale(stone, size)
        alist = [paper, scissors, stone]
        done = pygame.image.load('./素材/考卷/win.png')
        
        # 字型
        fontobj = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 150)
        smallfont = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 64)

        # 音效
        winsound = pygame.mixer.Sound('./素材/猜拳/勝利.mp3')
        losesound = pygame.mixer.Sound('./素材/猜拳/輸ㄌ.mp3')
        tiesound = pygame.mixer.Sound('./素材/猜拳/平手.mp3')
        
        choose = False # 有沒有出拳
        i = 0
        result = False
        word_pos = (430,97)
        score = 0
        plus = False
        minus = False
        finish = False
        run = True
        while run:

            # 畫背景
            screen.blit(bg, (0,0))
            
            # 顯示分數
            show_score = smallfont.render(str(score)+ '/3', True, (0,0,0))
            screen.blit(show_score, (530,20))
                 
            position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and choose == False and result == False and score < 3:
                        if 388 <= position[1] <= 586:
                            if 248 <= position[0] <= 474: # 布
                                choose = True
                                i = 0
                            if 474 <= position[0] <= 699: # 剪刀
                                choose = True
                                i = 1
                            if 699 <= position[0] <= 927: # 石頭
                                choose = True
                                i = 2
            
            if choose:
                duck = random.randint(0,2)
                screen.blit(alist[i], (600, 97))
                screen.blit(alist[duck], (350,97))
                pygame.display.update()
                pygame.time.delay(600)
                choose = False
                result = True

            if result:
                if duck == i:
                    tiesound.play()
                    tie = fontobj.render('TIE', True, (146,242,185))
                    screen.blit(tie, word_pos)
                if i - duck == 1 or (i == 0 and duck == 2):
                    winsound.play()
                    win = fontobj.render('WIN', True, (255,253,89))
                    screen.blit(win, word_pos)
                    plus = True
                if duck - i == 1 or (duck == 0 and i == 2):
                    losesound.play()
                    lose = fontobj.render('LOSE', True, (175,190,243))
                    screen.blit(lose, (380,97))
                    minus = True
                pygame.display.update()
                pygame.time.delay(1500)
                result = False
                pygame.event.clear() # 把多吃掉的東西清光
            
            if plus:
                score += 1
                plus = False
            if minus:
                score -= 1
                if score < 0:
                    score = 0
                minus = False
            
            if score == 3:
                finish = True
                screen.blit(bg, (0,0))
                show_score = smallfont.render(str(score)+ '/3', True, (0,0,0))
                screen.blit(show_score, (530,20))
                pygame.display.update()
                score += 1
                pygame.time.delay(1000)
            
            if finish:
                done = pygame.transform.smoothscale(done, (1120,630))
                screen.blit(done, (0,0))
            pygame.display.update()
    
    def byebyebell(self):
        
        # 載入音效
        ring = pygame.mixer.Sound('./素材/傅鐘/鐘聲.mp3')
        laugh = pygame.mixer.Sound('./素材/傅鐘/笑聲.mp3')
        
        # 載入圖片
        bg = pygame.image.load('./素材/傅鐘/傅鐘.jpg')
        bg = pygame.transform.smoothscale(bg, (320, 600))
        end = pygame.image.load('./素材/考卷/gameover.png')
        end = pygame.transform.smoothscale(end, (1120, 630))
        
        # 載入字
        fontobj = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 64)
        
        count = 0
        bell = False
        mock = False
        run = True
        while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            if bell == False:
                for i in range(21):
                    ring.play()
                    count += 1
                    total = fontobj.render(str(count)+'/21', True, (0,0,0))
                    # 畫背景
                    screen.fill((255,255,255))
                    screen.blit(bg, (400, 25))
                    screen.blit(total, (900,75))
                    pygame.display.update()
                    pygame.time.delay(1500)
                bell = True
            
            screen.blit(end, (0,0))
            pygame.display.update()
            pygame.time.delay(500)
            
            if mock == False:
                for k in range(2):
                    laugh.play()
                    pygame.time.delay(190)
                mock = True
        
            

# 玩遊戲
play = little_game()
play.guess_song()
pygame.quit()
