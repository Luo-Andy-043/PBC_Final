import pygame


class Array2D:
    """
        說明：
            1.構造方法需要兩個參數，即二維數組的寬和高
            2.成員變量w和h是二維數組的寬和高
            3.使用：‘對象[x][y]’可以直接取到相應的值
            4.數組的默認值都是0
    """

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = [[1 for y in range(h)] for x in range(w)]

    def showArray2D(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.data[x][y], end=' ')
            print("")

    def __getitem__(self, item):
        return self.data[item]


winSur = None  # 窗口的surface
map2d = None  # 地圖的二維數組
mapImg = None  # 地圖的圖片
x, y = [0, 0]  # 地圖當前繪圖座標
dirKeyState = [0, 0, 0, 0]  # 下，上，右，左方向鍵狀態，0沒按下 1按下


def init():
    global winSur, map2d, mapImg
    pygame.init()
    pygame.display.set_caption("地圖行走層編輯器")
    winSur = pygame.display.set_mode((920, 540))
    mapImg = pygame.image.load('C:\\Users\\asus\\Desktop\\新增資料夾\\地圖全圖_完稿_全.jpg')
    mapImg = pygame.transform.smoothscale(mapImg, (1350*2, 2250*2))
    # 以20*20像素爲一個可行走的格子
    map2d = Array2D(int(mapImg.get_width() / 20), int(mapImg.get_height() / 20))


def writeMap():
    with open('C:\\Users\\asus\\Desktop\\map.txt', mode='w', encoding='utf8') as file:
        file.write(str(map2d.data))
    print("保存地圖成功！")


def readMap():
    global map2d
    with open('C:\\Users\\asus\\Desktop\\map.txt', mode='r', encoding='utf8') as file:
        data = file.read()
    map2d.data = eval(data)
    map2d.w = len(map2d.data)
    map2d.h = len(map2d.data[0])
    print("讀取地圖成功！")


def moveMap():
    """
    移動地圖
    :return:
    """
    global x, y
    step = 20
    if dirKeyState[0] == 1:
        y += step
        if y + step > 0:
            y = 0

    if dirKeyState[1] == 1:
        y -= step
        if y - step < -(mapImg.get_height() - 540):
            y = -(mapImg.get_height() - 540)

    if dirKeyState[2] == 1:
        x += step
        if x + step > 0:
            x = 0

    if dirKeyState[3] == 1:
        x -= step
        if x - step < -(mapImg.get_width() - 920):
            x = -(mapImg.get_width() - 920)


def drawMap():
    """
    繪製不可行走區域
    :return:
    """
    for ty in range(map2d.h):
        for tx in range(map2d.w):
            if map2d[tx][ty] == 1:
                pygame.draw.rect(winSur, (0, 0, 0), (x + tx * 20 + 1, y + ty * 20 + 1, 14, 14), 1)


def mainLoop():
    global dirKeyState, map2d
    # 相關參數
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dirKeyState[0] = 1
                elif event.key == pygame.K_DOWN:
                    dirKeyState[1] = 1
                elif event.key == pygame.K_LEFT:
                    dirKeyState[2] = 1
                elif event.key == pygame.K_RIGHT:
                    dirKeyState[3] = 1
                elif event.key == pygame.K_r:
                    readMap()  # 讀取地圖
                elif event.key == pygame.K_w:
                    writeMap()  # 保存地圖
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    dirKeyState[0] = 0
                elif event.key == pygame.K_DOWN:
                    dirKeyState[1] = 0
                elif event.key == pygame.K_LEFT:
                    dirKeyState[2] = 0
                elif event.key == pygame.K_RIGHT:
                    dirKeyState[3] = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()  # 獲得當前鼠標座標
                map_x = mouse_x + (-x)
                map_y = mouse_y + (-y)
                cell_x = int(map_x / 20)
                cell_y = int(map_y / 20)
                if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠標左鍵按下
                    map2d[cell_x][cell_y] = 0
                if pygame.mouse.get_pressed() == (0, 0, 1):  # 鼠標左鍵按下
                    map2d[cell_x][cell_y] = 1
        pygame.time.delay(32)
        # 邏輯更新
        moveMap()
        # 繪圖更新
        winSur.blit(mapImg, (x, y))
        drawMap()
        pygame.display.flip()


if __name__ == '__main__':
    init()
    mainLoop()