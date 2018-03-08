
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
        pass
    # def ...
    def move(self,xdir,ydir):
        if self.x+xdir<DISP_WIDTH and self.x+xdir>0:
            if self.y+ydir<DISP_HEIGHT and self.y+ydir>0:
                self.x+=xdir
                self.y+=-ydir
                
    def draw(self, color, surf):
        pygame.draw.rect(surf,color,(self.x,self.y,10,10))
