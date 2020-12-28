# A lot of credits to Thomas Dubyak and Jeremy Morris on GitHub, the author of "Pykemon"
# https://github.com/ThomasDubyak/pykemon

""" 邏輯:

一次微分
不定積分
泰勒展開式
求x->0極限


解題順序：求極限->一次微分*2



要修的東西

1. 按鈕位置、圖片位置
2. 沒有延遲的問題
3. 更新的圖片（目前只有e^x）
4. 背景顏色（目前用預設的詭異綠色）
"""
###############################################################################



# 正文開始
import pygame, os, sys, time
working_path = os.path.dirname(__file__)
os.chdir(working_path)

# 定義指數函數的class
class Exponential():

    def __init__(self):
        self.health = 100  # 開始的血量
        self.status = "exponential^x"
        self.hit_count = 0 # 計算攻擊了幾次

    def transform_to_first(self):
        self.health -= 70
        self.status = "x+1"

    def transform_to_constant(self):
        self.health -= 20
        self.status = "1"

    def transform_to_zero(self):
        self.health -= 10
        self.status = "0"

# 血量條
class HealthBar():
#Class for creating unique healthbar objects for the enemy.
    def __init__(self,x,y):
  #Function for initializing the attributes of the healthbar. Location and healthbar
  #length.
        self.position = (x,y)
        self.negDimensions = (150,5)
        self.posDimensions = [150,5]
    def drawRects(self):
    #Function for drawing the actual rectangles that make up the health bar.
    #(x,y,width,height)
        pygame.draw.rect(DISPLAYSURF, RED, (self.position, self.negDimensions))
        pygame.draw.rect(DISPLAYSURF, GREEN, (self.position, self.posDimensions))
        pygame.display.update()
    def updateBar(self):
  #Function for determining the appropriate current length of the green portion of the
  #healthbar. Function first determines the proportion of remaining health for the
  #character, then applies that proportion to the original length to find the new
  #length.
        maxHealth = 100 # 指數的滿血
        currentHealth = enemy.health
        healthProportion = int(currentHealth)/int(maxHealth)
        newDimension = healthProportion*self.negDimensions[0]
        self.posDimensions[0] = newDimension

enemy = Exponential()       # 建立 Exponential 物件
enemyBar = HealthBar(410,35)      # 建立 Exponential 血量條


# 建立技能選項
skills = ["一次微分", "不定積分", "計量財務模型", "求x->0極限"]


# 管管頭跟指數的路徑
headPath = "./素材/指數/guanguan.png"
enemyPath = "./素材/指數/函數.png"




#COLORS
           #R    G    B
BLUE =     (0,   0,   255)
GREEN =    (0,   128, 0)
PURPLE =   (128, 0,   128)
RED =      (255, 0,   0)
YELLOW =   (255, 255, 0)
NAVYBLUE = (0,   0,   128)
WHITE =    (255, 255, 255)
BLACK =    (0,   0,   0)
ALPHA =    (255, 0,   255)

################################################################################
#Utility Functions
################################################################################

#？？？？？
def drawMoveText(text, font, surface, x, y, color):
#A text drawing function that is specifically modified to draw text around the
#center of the string rather than at the top left corner.
    textobj = font.render(text,12,color)
    textrect = textobj.get_rect()
    textrect.center = (x,y)
    surface.blit(textobj,textrect)
    pygame.display.update()



def redraw():
#This function contains a series of expressions that redraw every element of
#the battle screen in order from top to bottom.
# 需要修正位置"""
    DISPLAYSURF.blit(guanguanHead, (200,175))
    drawText("管管", font, DISPLAYSURF, 380, 260, BLACK)
    DISPLAYSURF.blit(enemyHead, (620, 0))
    drawText("邪惡的數學怪獸", font, DISPLAYSURF, 430, 45, BLACK)
    enemyBar.updateBar()
    enemyBar.drawRects()
    pygame.display.update()


# ?
def displayMessage(message):
# This function contains statements that use the text drawing functions in order
# with display clearing functions to clear the text area and redraw everything
# in an efficient manner.
    drawText(message, font, DISPLAYSURF, 10,400, BLACK)
    redraw()
    pygame.time.delay(10)
    DISPLAYSURF.blit(background, (0,0))


# OK
def drawText(text, font, surface, x, y, color):
#Simple function for drawing text onto the screen. Function contains expression
#for word wrap.
    if len(text) > 49:
        textLine1 = text[:48]
        textLine2 = text[48:]
    else:
        textLine1 = text
        textLine2 = ""

        textobj1 = font.render(textLine1,12,color)
        textrect1 = textobj1.get_rect()
        textrect1.topleft = (x,y)
        surface.blit(textobj1,textrect1)
        pygame.display.update()

        textobj2 = font.render(textLine2,1,color)
        textrect2 = textobj2.get_rect()
        textrect2.topleft = (x,y+10)
        surface.blit(textobj2,textrect2)
        pygame.display.update()


# OK (附註：這個東西好強，credits to Dubyak and Morris!!)
def animateText(text, font, surface, x, y, color):
#Function for printing text. The first block of code acts as a word wrap creator
#in the event that the string is too long to fit in the window. The animated portion
#is simply the act of adding each additional charcter after a tick in the FPS clock.
    if len(text) > 49:
        textLine1 = text[:49]
        textLine2 = text[48:]
    else:
        textLine1 = text
        textLine2 = ""
    i = 0
    for letter in textLine1:
        realLine1 = textLine1[:i]
        textobj1 = font.render(realLine1,1,color)
        textrect1 = textobj1.get_rect()
        textrect1.topleft = (x,y)
        surface.blit(textobj1,textrect1)
        pygame.display.update()
        fpsClock.tick(FPS)
    i += 1
    j = 0
    for letter in textLine2:
        realLine2 = textLine2[:j]
        textobj2 = font.render(textLine2,1,color)
        textrect2 = textobj2.get_rect()
        textrect2.topleft = (x,y+10)
        surface.blit(textobj2,textrect2)
        pygame.display.update()
        j += 1


# OK
class Button():
#Class for creating and maintaining unique buttons for a number of different
#purposes.
    def assignImage(self, picture):
  #function for handling the assignment of an image to each individual button object
        self.rect = picture.get_rect()
    def setCoords(self, x,y):
  #Function for handling the assignment of coordinates for each individual button
  #object
        self.rect.topleft = x,y
    def drawButton(self, picture):
  #Function for handling drawing the actual button on the screen
        DISPLAYSURF.blit(picture, self.rect)
    def pressed(self,mouse):
  #Function for determining whether or not a mouse click is inside a button object
        if self.rect.collidepoint(mouse) == True:
            return True

# OK
def pMoveSelect(pMoveList):
#The player move select function. This function draws the instructions and the
#buttons necessary to guide the player in selecting a move for their pokemon.

  #Redrawing background image to clear text
    DISPLAYSURF.blit(background, (0,0))
  #Drawing the prompt in the text section
    drawText("想要" + '\n' + "管管做什麼？", font, DISPLAYSURF, 10,400, BLACK)
    redraw()

  #Drawing buttons for use in the move selection process. Buttons are separate
  #from the text on the button to allow the system to be completely modular
    button1.drawButton(button)
    drawMoveText(pMoveList[0], font, DISPLAYSURF, 100, 499, BLACK)
    button2.drawButton(button)
    drawMoveText(pMoveList[1], font, DISPLAYSURF, 330, 499, BLACK)
    button3.drawButton(button)
    drawMoveText(pMoveList[2], font, DISPLAYSURF, 560, 566, BLACK)
    button4.drawButton(button)
    drawMoveText(pMoveList[3], font, DISPLAYSURF, 790, 566, BLACK)
    pygame.display.update()

  #Key listener block for the move selection process. When the mouse is clicked,
  #The button class checks to see if the mouse click was inside one of the buttons.
    unpicked = True
    while unpicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if button1.pressed(mouse) == True: #Is mouseclick on button?
                    pMove = skills[0] #assigning corresponding move as pMove
                    unpicked = False #modifying conditional to break iteration of loop
                if button2.pressed(mouse) == True:
                    pMove = skills[1]
                    unpicked = False
                if button3.pressed(mouse) == True:
                    pMove = skills[2]
                    unpicked = False
                if button4.pressed(mouse) == True:
                    pMove = skills[3]
                    unpicked = False

  #Function returns a list that contains all of the stats associated with the
  #selected move.
    return pMove

################################################################################
#Image Initialization Functions
################################################################################

# 只留一個參考

def SquirtImages():
  fileNames = ["squirtleFront.png","squirtleBack.png"]
  squirtArray = []
  for x in fileNames:
    newImg = pygame.image.load(x)
    squirtArray.append(newImg)
  return squirtArray

#All the code in this section is designed to load the images of the pokemon into
#lists that can be indexed. The lists these functions return are indexed in
#multiple locations throughout the program

################################################################################
#Main Loop Function
################################################################################


# 不確定寫了什麼
def Battle(pMoveList):


  #Entire following block of code dedicated to drawing the battle screen for the
  #first time in the correct order, and with good readability
    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(guanguanHead, (200,175))  # 改
    drawText('管管', font, DISPLAYSURF, 380, 260, BLACK)
    DISPLAYSURF.blit(background, (0,0))
    drawText("外星語言館派出了 e^x 函數!", font, DISPLAYSURF, 10,400, BLACK)
    DISPLAYSURF.blit(guanguanHead, (200,175))  # 改
    drawText('管管', font, DISPLAYSURF, 380, 260, BLACK)
    time.sleep(2)
    DISPLAYSURF.blit(background, (0,0))
    redraw()


    won = False
  #Main program loop. Loop terminates when one pokemon has fainted.
    while True:
    #Executing the move selection functions for both the player and the computer
        redraw()
        pMove = pMoveSelect(pMoveList)
        pygame.display.update()


        if enemy.hit_count >= 5:
            drawText("函數使出了致命一擊！", font, DISPLAYSURF, 10, 400, BLACK)
            drawText("你被擊敗了！", font, DISPLAYSURF, 10, 400, BLACK)
            break # 還不知道要怎麼接

        if enemy.status == "exponential^x":
            if pMove == skills[3]:
                TextToPrint = "效果十分顯著！"
                enemy.transform_to_first()
            elif pMove == skills[2]: # 泰勒展開？
                TextToPrint = "似乎沒什麼用..."
            else:
                TextToPrint = "似乎沒什麼用..."
                enemy.hit_count += 1 # 打了幾次

        elif enemy.status == "x+1":
            if pMove == skills[0]:
                TextToPrint = "效果十分顯著！"
                enemy.transform_to_constant()
            elif pMove == skills[2]: # 泰勒展開？
                TextToPrint = "效果十分顯著！"

            else:
                TextToPrint = "似乎沒什麼用..."
                enemy.hit_count += 1 # 打了幾次

        elif enemy.status == "1":
            if pMove == skills[0]:
                TextToPrint = "效果十分顯著！"
                enemy.transform_to_zero()
                won = True
            elif pMove == skills[2]: # 泰勒展開？
                TextToPrint = "效果十分顯著！"

        else:
            TextToPrint = "似乎沒什麼用..."
            enemy.hit_count += 1 # 打了幾次


        # 需要更改
        DISPLAYSURF.pygame.blit(background,(0,0))
        displayMessage(TextToPrint)
        enemyBar.updateBar()
        enemyBar.drawRects()
        pygame.display.update()

        if won:
            break


  #If the player won, player pokemon is displayed on the victory screen
    if won:
        DISPLAYSURF.blit(endBackground,(0,0))
        drawText("You won!", font, TEXTSURF, 120, 100, BLACK)
        pygame.display.update()


################################################################################
#Execution and Initialization
################################################################################

if __name__ == '__main__':

  #Pygame initialization statments. Defining basic attributes of game window
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((960, 540))
    TEXTSURF = pygame.display.set_mode((960,540))
    pygame.display.set_caption('ExpGame')
    fpsClock = pygame.time.Clock()
    FPS = 15
    font = pygame.font.Font('./素材/fonts/NotoSansCJKtc-hinted/NotoSansCJKtc-Black.otf', 24)
    guanguanHead = pygame.image.load(headPath).convert_alpha()
    guanguanHead = pygame.transform.smoothscale(guanguanHead, (170,140))

    enemyHead = pygame.image.load(enemyPath).convert_alpha()
    enemyHead = pygame.transform.smoothscale(enemyHead, (170,160))
  # Initalizing images for execution.
  # Type code here


  #Statements below initialize genergic image assets
    button = pygame.image.load("./素材/指數/button.png")
    background = pygame.image.load("./素材/指數/background.png")
    background = pygame.transform.smoothscale(background, (960, 540))


  #initializing the health bars for the enemy.
    enemyBar = HealthBar(10,35)


  #Initializing the buttons for player move selection each turn
    button1 = Button()
    button1.assignImage(button)
    button1.setCoords(2,468)
    button2 = Button()
    button2.assignImage(button)
    button2.setCoords(242,468)
    button3 = Button()
    button3.assignImage(button)
    button3.setCoords(482,468)
    button4 = Button()
    button4.assignImage(button)
    button4.setCoords(722,468)

  #Execution of the main loop of the program. More information on this function
  #can be found above.
    Battle(skills)
