import pygame,sys
from pygame.locals import *
from colors import *

class Character:

    def __init__(self,x,y):
        # la di da di da
        self.x=x
        self.y=y
        self.width = 10
        self.height = 10
        self.rect =  pygame.Rect((self.x,self.y,self.width,self.height))
    # def ...
    def move(self,xdir,ydir):
        self.x+=xdir
        self.y+=ydir
    def draw(self, surf):
        pygame.draw.rect(surf,RED,self.rect)
    def grow(self):
        self.width += 2
        self.height += 2
    def hitBy(self,rect):
        return self.rect.colliderect(rect)
