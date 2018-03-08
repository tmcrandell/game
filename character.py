
import pygame,sys, numpy
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
        if self.x+xdir<DISP_WIDTH and self.x+xdir>0:
            if self.y+ydir<DISP_HEIGHT and self.y+ydir>0:
                self.x+=xdir
                self.y+=-ydir
    
    def draw(self, color, surf):
        self.rect=pygame.Rect((self.x,self.y,self.width,self.height))
        pygame.draw.rect(surf,color,self.rect)
        
    def grow(self):
        self.width += 2
        self.height += 2
        
    def hitBy(self,rect):
        return self.rect.colliderect(rect)

    def relocate(self):
        self.x=numpy.random.randint(50,350)
        self.y=numpy.random.randint(50,350)

