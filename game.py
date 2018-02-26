#!/usr/bin/python

import pygame, sys
from pygame.locals import *

import colors, character
from colors import *

pygame.init()

# Global Constants
FPS = 30
DISP_WIDTH = 400
DISP_HEIGHT = 500
midStartX= 250
midStartY= 380
oStartX= 0

mid = character.Character(midStartX,midStartY)
officer = character.Character(100,100)
#snack = Snack()

fpsClock=pygame.time.Clock()

dispSURF=pygame.display.set_mode((DISP_WIDTH,DISP_HEIGHT),0,32)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # move guy down
                mid.move(0,-5)
            elif event.type == pygame.KEYUP:
                mid.move(0,5)
            elif event.type == pygame.K_LEFT:
                mid.move(-5,0)
            elif event.type == pygame.K_RIGHT:
                mid.move(5,0)
                # elif...
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        mid.draw(dispSURF)
        pygame.display.update()
        fpsClock.tick(FPS)


main()
