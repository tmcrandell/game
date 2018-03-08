
import pygame,sys
from pygame.locals import *
from colors import *

DISP_WIDTH = 400
DISP_HEIGHT = 500

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
<<<<<<< HEAD
        if self.x+xdir<DISP_WIDTH and self.x+xdir>0:
            if self.y+ydir<DISP_HEIGHT and self.y+ydir>0:
                self.x+=xdir
                self.y+=-ydir
                
    def draw(self, color, surf):
        pygame.draw.rect(surf,color,(self.x,self.y,10,10))
=======
        self.x+=xdir
        self.y+=ydir
    def draw(self, surf):
        pygame.draw.rect(surf,RED,self.rect)
    def grow(self):
        self.width += 2
        self.height += 2
    def hitBy(self,rect):
        return self.rect.colliderect(rect)
>>>>>>> c8d2d8a68f65fc25c3815a9bbdf1641da69a2d2b
