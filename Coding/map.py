import pygame, os
from setting import *

# 更正程式工作位置
working_path = os.path.dirname(__file__)
os.chdir(working_path)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
        self.map_data=[]
        for i in range(len(self.data)):
            self.map_data.append(self.data[i])
            #print(self.string)
        #print(self.data)
        #for i in range(len(self.data)):
        #    print(self.map_data[i])



class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)