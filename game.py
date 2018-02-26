import pygame, sys
from pygame.locals import *

import colors, character

pygame.init()

# Global Constants
FPS = 30
DISP_WIDTH = 400
DISP_HEIGHT = 500
midStartX= 250
midStartY= 380
oStartX=

mid = Character(midStartX,midStartY)
officer = Character()
snack = Snack()

fpsClock=pygame.time.Clock()

dispSURF=pygame.display.set_mode((DISP_WIDTH,DISP_HEIGHT),0,32)

def main():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # move guy down
            mid.move(0,-5)
        elif event.type == pygame.KEYUP:
            mid.move(0,5)
        elif event.type == pygame.KEYLEFT:
            mid.move(-5,0)
        elif event.type == pygame.KEYRIGHT:
            mid.move(5,0))
        # elif...
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    mid.draw(dispSURF)
    pygame.display.update()
    fpsClock.tick(FPS)
