import random, pygame, os

'''
打考卷:L
煎蛋:U
猜歌:E
打函數:F
曬太陽:S
'''


class little_game:

    def __init__(self, screen):

        self.screen = screen

    def mock_test(self):
        # 載入圖片
        rulepic = pygame.image.load('./素材/考卷/考卷規則.png')
        rulepic = pygame.transform.smoothscale(rulepic, (960, 540))
        pic0 = pygame.image.load('./素材/考卷/0.png')
        pic1 = pygame.image.load('./素材/考卷/1.png')
        pic2 = pygame.image.load('./素材/考卷/2.png')
        pic3 = pygame.image.load('./素材/考卷/3.png')
        pic4 = pygame.image.load('./素材/考卷/4.png')
        pic5 = pygame.image.load('./素材/考卷/5.png')
        end = pygame.image.load('./素材/考卷/gameover1.png')
        win = pygame.image.load('./素材/考卷/win.png')
        paper = pygame.image.load('./素材/考卷/紙條.jpg')
        test = [pic0, pic1, pic2, pic3, pic4, pic5]
        talk = pygame.image.load('./素材/考卷/talk.png')
        talk = pygame.transform.smoothscale(talk, (960,540))

        # 載入音效
        write = pygame.mixer.Sound('./素材/考卷/寫字.mp3')

        # MainLoop
        died = False
        rule = True
        said = False
        over = False
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if rule == True:
                            rule = False
                        if died == True:
                            # 再玩一次
                            hit = 0
                            add = 0
                            i = 3
                            died = False
                        if over:
                            run = False  # 顯示紙條，點一下離開

            if rule:
                self.screen.blit(rulepic, (0,0))
                pygame.display.update()
            else:
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
                        test[i] = pygame.transform.smoothscale(test[i], (960,540))
                        self.screen.blit(test[i], (0,0))
                        pygame.draw.rect(self.screen, (102,51,0), [80, 425, 800, 40], 0)
                        pygame.draw.rect(self.screen, (102,51,0), [280, 465, 40, 55], 0)
                        pygame.draw.rect(self.screen, (102,51,0), [680, 465, 40, 55], 0)
                        pygame.display.update()

                # 到頂ㄌ就掰掰
                elif i > 5:
                    died = True
                    end = pygame.transform.smoothscale(end, (960,540))
                    self.screen.blit(end, (0,0))
                    pygame.display.update()
                    run = False # 結束遊戲
                    pygame.time.delay(1500)
                    return 'lose'
                    pygame.display.update()  # press to retry

                # 寫完就贏ㄌ 耶
                else:
                    over = True
                    if said == False:
                        self.screen.blit(talk, (0,0))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        said = True
                    paper = pygame.transform.smoothscale(paper, (960,540))
                    self.screen.blit(paper, (0,0))
                    pygame.display.update()
                    run = False # 結束遊戲
                    note = pygame.image.load('../視覺設計/紙條.jpg').convert_alpha()
                    note = pygame.transform.smoothscale(note, (self.screen.get_size()))
                    self.screen.blit(note, (0,0))
                    pygame.time.delay(1500)
                    return 'win'

    def egg_game(self):
        story_1 = pygame.image.load('./素材/煎蛋/after_game_1.png').convert_alpha()
        story_2 = pygame.image.load('./素材/煎蛋/after_game_2.png').convert_alpha()
        story_1 = pygame.transform.smoothscale(story_1, (self.screen.get_size()))
        story_2 = pygame.transform.smoothscale(story_2, (self.screen.get_size()))
        switcher = [story_1, story_2]

        move_egg = False
        move_ok_egg = False
        egg_pos = 0, 0
        okegg_pos = 240,370
        egg_appear = False
        raw_egg_appear = False
        ok_egg_appear = False
        cook = 0
        wait = 0
        eaten = 0
        said = False
        run = True
        # 載入圖片
        rulepic = pygame.image.load('./素材/煎蛋/煎蛋規則.png').convert_alpha()
        rulepic = pygame.transform.smoothscale(rulepic, (960, 540))
        kitchen = pygame.image.load('./素材/煎蛋/背景.png').convert_alpha()
        kitchen = pygame.transform.smoothscale(kitchen, (960, 540))
        egg = pygame.image.load('./素材/煎蛋/生蛋.png').convert_alpha()
        raw_egg = pygame.image.load('./素材/煎蛋/生荷包蛋.png').convert_alpha()
        ok_egg = pygame.image.load('./素材/煎蛋/熟荷包蛋.png').convert_alpha()
        bite1 = pygame.image.load('./素材/煎蛋/咬1.png').convert_alpha()
        bite1 = pygame.transform.smoothscale(bite1, (135,100))
        bite2 = pygame.image.load('./素材/煎蛋/咬2.png').convert_alpha()
        bite2 = pygame.transform.smoothscale(bite2, (135,100))
        win = pygame.image.load('./素材/考卷/win.png').convert_alpha()

        # 載入音效
        swallow = pygame.mixer.Sound('./素材/煎蛋/吞.mp3')
        swallow.set_volume(1)
        fry = pygame.mixer.Sound('./素材/煎蛋/煎蛋.mp3')
        fry.set_volume(0.2)

        # 載入字
        fontobj = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 64)

        finish = False
        show = True
        rule = True
        while run:
            if rule:
                self.screen.blit(rulepic, (0,0))
            else:
                # 畫廚房背景
                self.screen.blit(kitchen, (0,0))

                # 顯示已吃幾顆
                score = fontobj.render(str(eaten)+'/5', True, (0,0,0), (255,255,255))
                self.screen.blit(score, (800,50))

                if eaten == 5:
                    if show:
                        pygame.display.update()
                        show = False
                    if said == False:
                        pygame.time.delay(1000)
                        win = pygame.transform.smoothscale(win, (960,540))
                        self.screen.blit(win, (0,0))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        said = True
                    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                position = pygame.mouse.get_pos()
                # 如果在蛋區點一下就會出現一顆蛋
                if event.type == pygame.MOUSEBUTTONDOWN and eaten < 5:
                    if rule == True:
                        if event.button == 1:
                            rule = False
                    if 674 <= position[0] <= 868 and 286 <= position[1] <= 479 and raw_egg_appear == False and ok_egg_appear == False:
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
                        if said == True:
                            run = False  # 顯示提示時點一下關閉

            if move_egg:
                egg_pos = pygame.mouse.get_pos()

            if egg_appear:
                egg = pygame.transform.smoothscale(egg, (135, 100))
                self.screen.blit(egg, (egg_pos[0]-67.5, egg_pos[1]-50))

            # 如果打蛋拖到鍋子上放開 蛋就會變成生荷包蛋
            if 136 <= egg_pos[0] <= 336 and 270 <= egg_pos[1] <= 469 and move_egg == False:
                    egg_appear = False
                    raw_egg_appear = True

            # 計時煮了多久
            if raw_egg_appear:
                cook += 1

            # 煮一段時間之後生蛋就會變熟蛋
            if raw_egg_appear and cook <= 140:
                raw_egg = pygame.transform.smoothscale(raw_egg, (135, 100))
                self.screen.blit(raw_egg, (170,320))
                fry.play()
            elif raw_egg_appear and cook > 140:
                ok_egg_appear = True
                okegg_pos = 240,370
                fry.stop()

            # 熟了之後動蛋
            if move_ok_egg:
                okegg_pos = pygame.mouse.get_pos()

            # 蛋進嘴巴
            if 387 <= okegg_pos[0] <= 574 and 149 <= okegg_pos[1] <= 208:
                ok_egg_appear = False
                raw_egg_appear = False
                eaten += 1
                # 吃蛋囉
                swallow.play()
                self.screen.blit(kitchen, (0,0))
                self.screen.blit(bite1, (413,160))
                self.screen.blit(score, (800,50))
                pygame.display.update()
                pygame.time.delay(500)
                swallow.play()
                self.screen.blit(kitchen, (0,0))
                self.screen.blit(bite2, (413,128.5))
                self.screen.blit(score, (800,50))
                pygame.display.update()
                pygame.time.delay(500)
                swallow.play()
                self.screen.blit(kitchen, (0,0))
                self.screen.blit(score, (800,50))
                pygame.display.update()
                # 回到最一開始ㄉ狀態
                move_egg = False
                move_ok_egg = False
                egg_pos = 0, 0
                okegg_pos = 240,370
                egg_appear = False
                raw_egg_appear = False
                ok_egg_appear = False
                cook = 0

            # 蛋還沒進嘴巴
            if ok_egg_appear:
                ok_egg = pygame.transform.smoothscale(ok_egg, (135, 100))
                self.screen.blit(ok_egg, (okegg_pos[0]-67.5, okegg_pos[1]-50))

            pygame.display.update()

        waiting = True
        index = 0
        self.screen.blit(switcher[index], (0,0))
        pygame.display.update()
        while waiting:
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        index += 1
                        if index >= 2:
                            waiting = False
                        else:
                            self.screen.blit(switcher[index], (0,0))
                            pygame.display.update()

        return 'win'

    def guess_song(self):

        # 載入圖片
        rulepic = pygame.image.load('./素材/猜歌/猜歌規則.png')
        rulepic = pygame.transform.smoothscale(rulepic, (960, 540))
        machine = pygame.image.load('./素材/猜歌/機器.png')
        wrong = pygame.image.load('./素材/猜歌/叉.png')
        wrong = pygame.transform.smoothscale(wrong, (100,100))
        right = pygame.image.load('./素材/猜歌/圈.png')
        right = pygame.transform.smoothscale(right, (100,100))

        # 載入音樂
        lowbou = pygame.mixer.Sound('./素材/猜歌/拔蘿蔔前奏.mp3')
        lowbou.set_volume(0.5)
        three = pygame.mixer.Sound('./素材/猜歌/三輪車前奏.mp3')
        three.set_volume(0.3)
        doggy = pygame.mixer.Sound('./素材/猜歌/哈巴狗前奏.mp3')
        doggy.set_volume(1)
        yes = pygame.mixer.Sound('./素材/猜歌/正確.mp3')
        yes.set_volume(0.3)
        no = pygame.mixer.Sound('./素材/猜歌/答錯.mp3')
        no.set_volume(0.8)

        # 字型
        fontobj = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 40)

        # 顏色
        normal = (102,51,0)
        light = (216,176,136)
        white = (255,255,255)

        rule = True
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
        played = False
        done = False
        run = True
        while run:
            # 畫背景
            self.screen.fill((252,245,216))
            machine = pygame.transform.smoothscale(machine, (378,415))
            self.screen.blit(machine, (15,40))
            position = pygame.mouse.get_pos()
            win = pygame.image.load('./素材/考卷/win.png')

            # 每一題點四個選項出現圈或叉
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        rule = False
                        if Q1:
                            if 15 <= position[0] <= 393 and 40 <= position[1] <= 455: # 點留聲機可以重播音樂
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
                            if -39 <= position[0] <= 339 and 140 <= position[1] <= 555:
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
                            if -39 <= position[0] <= 339 and 140 <= position[1] <= 555:
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

            if rule:
                self.screen.blit(rulepic, (0,0))
            else:
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
                if 356 <= position[0] <= 606 and 230 <= position[1] <= 313:
                    pygame.draw.rect(self.screen, light, [356, 230, 250, 83], 0)
                    option1 = True
                else:
                    pygame.draw.rect(self.screen, normal, [356, 230, 250, 83], 0)
                    option1 = False
                # option2
                if 656 <= position[0] <= 906 and 230 <= position[1] <= 313:
                    pygame.draw.rect(self.screen, light, [656, 230, 250, 83], 0)
                    option2 = True
                else:
                    pygame.draw.rect(self.screen, normal, [656, 230, 250, 83], 0)
                    option2 = False
                # option3
                if 356 <= position[0] <= 606 and 343 <= position[1] <= 426:
                    pygame.draw.rect(self.screen, light, [356, 343, 250, 83], 0)
                    option3 = True
                else:
                    pygame.draw.rect(self.screen, normal, [356, 343, 250, 83], 0)
                    option3 = False
                # option4
                if 656 <= position[0] <= 906 and 343 <= position[1] <= 426:
                    pygame.draw.rect(self.screen, light, [656, 343, 250, 83], 0)
                    option4 = True
                else:
                    pygame.draw.rect(self.screen, normal, [656, 343, 250, 83], 0)
                    option4 = False

                # 題目
                if Q1:
                    answer11 = fontobj.render('拔蘿蔔', True, white)
                    self.screen.blit(answer11,(426,240))
                    answer12 = fontobj.render('火車快飛', True, white)
                    self.screen.blit(answer12,(706,240))
                    answer13 = fontobj.render('小星星', True, white)
                    self.screen.blit(answer13,(426,353))
                    answer14 = fontobj.render('小蜜蜂', True, white)
                    self.screen.blit(answer14,(726,353))
                if Q2:
                    answer11 = fontobj.render('捕魚歌', True, white)
                    self.screen.blit(answer11,(426,240))
                    answer12 = fontobj.render('兩隻老虎', True, white)
                    self.screen.blit(answer12,(706,240))
                    answer13 = fontobj.render('三輪車', True, white)
                    self.screen.blit(answer13,(426,353))
                    answer14 = fontobj.render('潑水歌', True, white)
                    self.screen.blit(answer14,(726,353))
                if Q3:
                    answer11 = fontobj.render('虎姑婆', True, white)
                    self.screen.blit(answer11,(426,240))
                    answer12 = fontobj.render('春神來了', True, white)
                    self.screen.blit(answer12,(706,240))
                    answer13 = fontobj.render('茉莉花', True, white)
                    self.screen.blit(answer13,(426,353))
                    answer14 = fontobj.render('哈巴狗', True, white)
                    self.screen.blit(answer14,(726,353))

                # 點擊選項回應
                if correct1:
                    yes.play()
                    self.screen.blit(right, (306,221))
                    pygame.display.update()
                    pygame.time.delay(3100)
                    correct1 = False
                    Q1 = False
                    Q2 = True
                    played = False
                    pygame.event.clear()

                if correct2:
                    yes.play()
                    self.screen.blit(right, (306,334))
                    pygame.display.update()
                    pygame.time.delay(3100)
                    correct2 = False
                    Q2 = False
                    Q3 = True
                    played = False
                    pygame.event.clear()

                if correct3:
                    yes.play()
                    self.screen.blit(right, (606,334))
                    pygame.display.update()
                    pygame.time.delay(3100)
                    correct3 = False
                    done = True
                    pygame.event.clear()

                if done: # 三題都答完ㄌ
                    self.old_talk()

                    win = pygame.transform.smoothscale(win, (960,540))
                    self.screen.blit(win, (0,0))
                    pygame.display.update()
                    run = False
                    pygame.time.delay(1500)


                if wrong1:
                    no.play()
                    self.screen.blit(wrong, (306,221))
                    pygame.display.update()
                    pygame.time.delay(700)
                    wrong1 = False
                    pygame.event.clear()

                if wrong2:
                    no.play()
                    self.screen.blit(wrong, (606,221))
                    pygame.display.update()
                    pygame.time.delay(700)
                    wrong2 = False
                    pygame.event.clear()

                if wrong3:
                    no.play()
                    self.screen.blit(wrong, (306,334))
                    pygame.display.update()
                    pygame.time.delay(700)
                    wrong3 = False
                    pygame.event.clear()

                if wrong4:
                    no.play()
                    self.screen.blit(wrong, (606,334))
                    pygame.display.update()
                    pygame.time.delay(700)
                    wrong4 = False
                    pygame.event.clear()

            pygame.display.update()
        return 'win'

    def beatduck(self):
        size = (200,200)
        # 載入圖片
        rulepic = pygame.image.load('./素材/猜拳/猜拳規則.png')
        rulepic = pygame.transform.smoothscale(rulepic, (960, 540))
        back = pygame.image.load('./素材/猜拳/背景.png')
        back = pygame.transform.smoothscale(back, (960,540))
        stonebig = pygame.image.load('./素材/猜拳/中石頭.png')
        stonebig = pygame.transform.smoothscale(stonebig, (152,165))
        paperbig = pygame.image.load('./素材/猜拳/中布.png')
        paperbig = pygame.transform.smoothscale(paperbig, (156,165))
        scissorsbig = pygame.image.load('./素材/猜拳/中剪刀.png')
        scissorsbig = pygame.transform.smoothscale(scissorsbig, (122,165))
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

        rule = True
        choose = False # 有沒有出拳
        i = 0
        result = False
        score = 0
        plus = False
        minus = False
        finish = False
        run = True
        while run:

            position = pygame.mouse.get_pos()
            # 畫背景
            self.screen.blit(back, (0,0))

            if  332 <= position[1] <= 503:
                if 213 <= position[0] <= 406:
                    self.screen.blit(paperbig, (233,335))
                elif 406 <= position[0] <= 600:
                    self.screen.blit(scissorsbig, (442,335))
                elif 600 <= position[0] <= 794:
                    self.screen.blit(stonebig, (621,335))

            # 顯示分數
            show_score = smallfont.render(str(score)+ '/3', True, (0,0,0))
            self.screen.blit(show_score, (451,20))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        rule = False
                        if choose == False and result == False and score < 3:
                            if 332 <= position[1] <= 503:
                                if 213 <= position[0] <= 406: # 布
                                    choose = True
                                    i = 0
                                if 406 <= position[0] <= 600: # 剪刀
                                    choose = True
                                    i = 1
                                if 600 <= position[0] <= 794: # 石頭
                                    choose = True
                                    i = 2

            if rule:
                self.screen.blit(rulepic, (0,0))
            else:
                if choose:
                    duck = random.randint(0,2)
                    self.screen.blit(alist[i], (521, 97))
                    self.screen.blit(alist[duck], (271,97))
                    pygame.display.update()
                    pygame.time.delay(600)
                    choose = False
                    result = True

                if result:
                    if duck == i:
                        tiesound.play()
                        tie = fontobj.render('TIE', True, (146,242,185))
                        self.screen.blit(tie, (373,97))
                    if i - duck == 1 or (i == 0 and duck == 2):
                        winsound.play()
                        win = fontobj.render('WIN', True, (255,253,89))
                        self.screen.blit(win, (351,97))
                        plus = True
                    if duck - i == 1 or (duck == 0 and i == 2):
                        losesound.play()
                        lose = fontobj.render('LOSE', True, (175,190,243))
                        self.screen.blit(lose, (301,97))
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
                    self.screen.blit(back, (0,0))
                    show_score = smallfont.render(str(score)+ '/3', True, (0,0,0))
                    self.screen.blit(show_score, (451,20))
                    pygame.display.update()
                    score += 1
                    pygame.time.delay(1000)

                if finish:
                    done = pygame.transform.smoothscale(done, (960,540))
                    self.screen.blit(done, (0,0))
                    run = False
                    pygame.display.update()
                    pygame.time.delay(1500)
            pygame.display.update()

    def byebyebell(self):

        # 載入音效
        ring = pygame.mixer.Sound('./素材/傅鐘/鐘聲.mp3')
        laugh = pygame.mixer.Sound('./素材/傅鐘/笑聲.mp3')

        # 載入圖片
        back = pygame.image.load('./素材/傅鐘/傅鐘.jpg')
        back = pygame.transform.smoothscale(back, (266, 500))
        end = pygame.image.load('./素材/傅鐘/報應.png')
        end = pygame.transform.smoothscale(end, (960, 540))

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and bell == True:
                        run = False

            if bell == False:
                ring.play()
                count += 1
                total = fontobj.render(str(count)+'/21', True, (0,0,0))
                # 畫背景
                self.screen.fill((255,255,255))
                self.screen.blit(back, (347, 20))
                self.screen.blit(total, (720,25))
                pygame.display.update()
                pygame.time.delay(1500)

            if count == 21:
                bell = True
                self.screen.blit(end, (0,0))
                pygame.display.update()

                if mock == False:
                    for k in range(2):
                        laugh.play()
                        pygame.time.delay(190)
                    mock = True
        return 'lose'

    def hitmath(self):
        # 載入圖片

        rule = pygame.image.load('./素材/e^x/指數規則.png').convert_alpha()
        rule = pygame.transform.smoothscale(rule, (960,540))
        bg = pygame.image.load('./素材/指數/背景.png').convert_alpha()
        bg = pygame.transform.smoothscale(bg, (960,540))
        myhead = pygame.image.load('./素材/指數/guanguan.png').convert_alpha()
        myhead = pygame.transform.scale(myhead, (172,200))
        e = pygame.image.load('./素材/e^x/e^x（去背）.png').convert_alpha()
        e = pygame.transform.scale(e, (360,200))
        xone = pygame.image.load('./素材/e^x/x+1.png').convert_alpha()
        xone = pygame.transform.scale(xone, (360,200))
        one = pygame.image.load('./素材/e^x/1.png').convert_alpha()
        one = pygame.transform.scale(one, (151,200))
        fire = pygame.image.load('./素材/e^x/火.png').convert_alpha()
        fire = pygame.transform.scale(fire, (151,200))

        # 載入字型
        fontobj = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 30)

        # 載入音效
        explode = pygame.mixer.Sound('./素材/e^x/火聲.ogg')
        tada = pygame.mixer.Sound('./素材/e^x/登場.mp3')
        scream1 = pygame.mixer.Sound('./素材/e^x/尖叫1.mp3')
        scream1.set_volume(0.5)
        scream2 = pygame.mixer.Sound('./素材/e^x/尖叫2.mp3')
        scream2.set_volume(0.5)
        scream3 = pygame.mixer.Sound('./素材/e^x/尖叫3.mp3')
        scream3.set_volume(0.5)
        bad = pygame.mixer.Sound('./素材/e^x/壞笑.mp3')

        part1 = True
        part2 = False
        part3 = False
        option1 = False  # 一次微分
        option2 = False  # 不定積分
        option3 = False  # 計量財務模型
        option4 = False  # 極限
        stage1 = False
        stage2 = False
        stage3 = False
        success1 = False
        success2 = False
        success3 = False
        fail = False
        black = (0,0,0)
        linepos = (50,328)
        finish = False
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if part1:
                            part1 = False
                            part2 = True
                        if stage1:
                            if option4:
                                success1 = True
                            elif option2 or option3 or option1:
                                fail = True
                        if stage2:
                            if option1:
                                success2 = True
                            elif option2 or option3 or option4:
                                fail = True
                        if stage3:
                            if option1:
                                success3 = True
                            elif option2 or option3 or option4:
                                fail = True

            pygame.display.update()

            if part1:
                self.screen.blit(rule, (0,0))
            if part2:
                self.screen.blit(bg, (0,0))
                self.screen.blit(myhead, (155,120))
                pygame.draw.rect(self.screen, (223,225,205), [0, 430, 960, 108], 0)
                say = fontobj.render('外星語言館派出了函數怪物！', True, black)
                # first.play()
                self.screen.blit(say, linepos)
                pygame.display.update()
                pygame.time.delay(500)
                self.screen.blit(e, (500,25))
                self.screen.blit(say, linepos)
                pygame.display.update()
                pygame.time.delay(500)
                self.screen.blit(e, (500,25))
                tada.play()
                pygame.time.delay(200)
                pygame.display.update()
                pygame.time.delay(300)
                pygame.time.delay(2300)
                self.screen.blit(bg, (0,0))
                self.screen.blit(e, (500,25))
                self.screen.blit(myhead, (155,120))
                pygame.draw.rect(self.screen, (223,225,205), [0, 430, 960, 108], 0)
                say = fontobj.render('打倒它！', True, black)
                self.screen.blit(say, linepos)
                pygame.display.update()
                pygame.time.delay(2000)
                part2 = False
                part3 = True
                stage1 = True

            elif part3:
                # 繪製背景
                self.screen.blit(bg, (0,0))

                # 畫管管
                self.screen.blit(myhead, (155,120))

                # 畫數學
                if stage1:
                    self.screen.blit(e, (500,25))
                if stage2:
                    self.screen.blit(xone, (515,25))
                if stage3:
                    self.screen.blit(one, (625,25))
                # 畫台詞
                always = fontobj.render('想要管管做什麼？', True, black)
                self.screen.blit(always, linepos)

                # 畫選項
                option1wd = fontobj.render('一次微分', True, black)
                option2wd = fontobj.render('不定積分', True, black)
                option3wd = fontobj.render('計量財務模型', True, black)
                option4wd = fontobj.render('求x→0極限', True, black)
                self.screen.blit(option1wd, (87,453))
                self.screen.blit(option2wd, (316,453))
                self.screen.blit(option3wd, (513,453))
                self.screen.blit(option4wd, (752,453))

            if fail:
                line = fontobj.render('似乎沒什麼用...', True, black, (225,230,170))
                self.screen.blit(line, linepos)
                pygame.display.update()
                bad.play()
                pygame.time.delay(1500)
                fail = False
                pygame.event.clear()

            if success1:
                line = fontobj.render('效果十分顯著！', True, black, (225,230,170))
                self.screen.blit(bg, (0,0))
                self.screen.blit(e, (500,25))
                self.screen.blit(fire,(625,25))
                self.screen.blit(line, linepos)
                self.screen.blit(option1wd, (87,453))
                self.screen.blit(option2wd, (316,453))
                self.screen.blit(option3wd, (513,453))
                self.screen.blit(option4wd, (752,453))
                self.screen.blit(myhead, (155,120))
                pygame.display.update()
                explode.play()
                scream1.play()
                pygame.time.delay(2100)
                stage1 = False
                stage2 = True
                success1 = False
                pygame.event.clear()

            if success2:
                line = fontobj.render('效果十分顯著！', True, black, (225,230,170))
                self.screen.blit(bg, (0,0))
                self.screen.blit(xone, (515,25))
                self.screen.blit(fire,(625,25))
                self.screen.blit(line, linepos)
                self.screen.blit(option1wd, (87,453))
                self.screen.blit(option2wd, (316,453))
                self.screen.blit(option3wd, (513,453))
                self.screen.blit(option4wd, (752,453))
                self.screen.blit(myhead, (155,120))
                pygame.display.update()
                explode.play()
                scream2.play()
                pygame.time.delay(1500)
                stage2 = False
                stage3 = True
                success2 = False
                pygame.event.clear()

            if success3:
                line = fontobj.render('效果十分顯著！', True, black, (225,230,170))
                self.screen.blit(bg, (0,0))
                self.screen.blit(one, (625,25))
                self.screen.blit(fire,(625,25))
                self.screen.blit(line, linepos)
                self.screen.blit(option1wd, (87,453))
                self.screen.blit(option2wd, (316,453))
                self.screen.blit(option3wd, (513,453))
                self.screen.blit(option4wd, (752,453))
                self.screen.blit(myhead, (155,120))
                pygame.display.update()
                explode.play()
                scream3.play()
                pygame.time.delay(2100)
                stage3 = False
                success3 = False
                self.screen.blit(bg, (0,0))
                self.screen.blit(option1wd, (87,453))
                self.screen.blit(option2wd, (316,453))
                self.screen.blit(option3wd, (513,453))
                self.screen.blit(option4wd, (752,453))
                self.screen.blit(myhead, (155,120))
                pygame.display.update()
                pygame.time.delay(1500)
                run = False
                pygame.event.clear()

            position = pygame.mouse.get_pos()
            if 447 <= position[1] <= 513:
                if 31 <= position[0] <= 251:
                    option1 = True
                else:
                    option1 = False
                if 262 <= position[0] <= 481:
                    option2 = True
                else:
                    option2 = False
                if 490 <= position[0] <= 709:
                    option3 = True
                else:
                    option3 = False
                if 717 <= position[0] <= 937:
                    option4 = True
                else:
                    option4 = False

            pygame.display.update()
        return 'win'

    def old_talk(self):
        sentence0 = pygame.image.load('./素材/老人的話/words1.png').convert_alpha()
        sentence0 = pygame.transform.smoothscale(sentence0, (960,540))
        sentence1 = pygame.image.load('./素材/老人的話/words1.png').convert_alpha()
        sentence1 = pygame.transform.smoothscale(sentence1, (960,540))
        sentence2 = pygame.image.load('./素材/老人的話/words2.png').convert_alpha()
        sentence2 = pygame.transform.smoothscale(sentence2, (960,540))
        sentence3 = pygame.image.load('./素材/老人的話/words3.png').convert_alpha()
        sentence3 = pygame.transform.smoothscale(sentence3, (960,540))
        sentence4 = pygame.image.load('./素材/老人的話/words4.png').convert_alpha()
        sentence4 = pygame.transform.smoothscale(sentence4, (960,540))
        sentence5 = pygame.image.load('./素材/老人的話/words5.png').convert_alpha()
        sentence5 = pygame.transform.smoothscale(sentence5, (960,540))
        hint = pygame.image.load('./素材/猜歌/提示.png').convert_alpha()
        hint = pygame.transform.smoothscale(hint, (960,540))
        alist = [sentence0, sentence1, sentence2, sentence3, sentence4, sentence5, hint]
        
        # 音效
        old11 = pygame.mixer.Sound('./素材/老人的話/講古1-1.mp3')
        old12 = pygame.mixer.Sound('./素材/老人的話/講古1-2.mp3')
        old21 = pygame.mixer.Sound('./素材/老人的話/講古2-1.mp3')
        old22 = pygame.mixer.Sound('./素材/老人的話/講古2-2.mp3')
        old31 = pygame.mixer.Sound('./素材/老人的話/講古3-1.mp3')
        old32 = pygame.mixer.Sound('./素材/老人的話/講古3-2.mp3')

        i = 0
        run = True
        while run:
            self.screen.blit(alist[i], (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if i <= 5:
                            i += 1
                        else:
                            run = False
        return 'win'

    def sun_by_the_lake(self):

        pygame.init()

        # The PATHSSSSS!
        bg_path = "./素材/曬太陽/北北曬太陽.PNG"
        duck_path = "./素材/曬太陽/鴨鴨腳踏車（去背）.png"
        button_light_path = "./素材/曬太陽/find_bike_light.png"
        button_dark_path = "./素材/曬太陽/find_bike_dark.png"

        # 載入圖片
        sun_background = pygame.image.load(bg_path).convert_alpha()
        sun_background = pygame.transform.smoothscale(sun_background, (960, 540))

        duck_img = pygame.image.load(duck_path).convert_alpha()
        duck_img = pygame.transform.smoothscale(duck_img, (300,240)) # 待補,要轉換

        # Button 1288*450 真實

        button_light = pygame.image.load(button_light_path).convert_alpha()
        button_light = pygame.transform.smoothscale(button_light, (220,120))

        button_dark = pygame.image.load(button_dark_path).convert_alpha()
        button_dark = pygame.transform.smoothscale(button_dark, (220,120))

        # 設定一些座標
        BUTTON_COORDS = (700,320)
        duck_pos = (0,320)  # For moving purposes

        # 建立鴨子跟按鈕 Rect 物件
        button = pygame.Rect(BUTTON_COORDS[0], BUTTON_COORDS[1], 220, 120)

        self.screen.blit(sun_background, (0,0))
        pygame.display.update()

        run = True
        show_button = False
        stage1 = True
        stage2 = False
        start = pygame.time.get_ticks() / 1000
        while run:


            pygame.time.Clock().tick(100) # 快速迴圈

            time_elapsed = pygame.time.get_ticks() / 1000
            time_past = time_elapsed - start
            mousedown = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                   mousedown = True

                # 變色迴圈，偷放
            if show_button and stage1:
                if button.collidepoint(mouse_position):
                    button_img = button_light
                    self.screen.blit(button_img, BUTTON_COORDS)
                    pygame.display.update()

                else:
                    button_img = button_dark
                    self.screen.blit(button_img, BUTTON_COORDS)
                    pygame.display.update()


            mouse_position = pygame.mouse.get_pos()


            if time_past > 10 and stage1 and not show_button:
                show_button = True
                button_img = button_dark
                self.screen.blit(button_img, BUTTON_COORDS) # 待補座標
                pygame.display.update()

            if mousedown and button.collidepoint(mouse_position) and stage1:
                self.byebyebell()

            elif time_past > 15 and not stage2:
                stage1 = False
                stage2 = True
                self.screen.blit(sun_background, (0,0))


            elif time_past > 16 and stage2:
                duck_pos = (duck_pos[0] + 1, duck_pos[1])
                button = pygame.Rect(duck_pos[0], duck_pos[1], 300, 240)
                self.screen.blit(sun_background, (0,0))
                self.screen.blit(duck_img, duck_pos)
                pygame.display.update()


                if mousedown and button.collidepoint(mouse_position):
                    self.beatduck()
                    run = False

            pygame.display.update()
