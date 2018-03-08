#!/usr/bin/python

import pygame, sys, numpy
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
snack = character.Character(numpy.random.randint(0,DISP_WIDTH),numpy.random.randint(0,DISP_HEIGHT))
snack2= character.Character(numpy.random.randint(0,DISP_WIDTH),numpy.random.randint(0,DISP_HEIGHT))


fpsClock=pygame.time.Clock()

dispSURF=pygame.display.set_mode((DISP_WIDTH,DISP_HEIGHT),0,32)

def main():
    score=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mid.move(0,10)
                elif event.key == pygame.K_LEFT:
                    mid.move(-10,0)
                elif event.key == pygame.K_RIGHT:
                    mid.move(10,0)
                elif event.key == pygame.K_DOWN:
                    mid.move(0,-10)
                #elif...
                
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if snack.hitBy(mid):
            snack.relocate()
            mid.grow()
            score+=1

        if snack2.hitBy(mid):
            snack2.relocate()
            mid.grow()
            score+=1

        if score==10:
            print "you win"
            break            
                        
        dispSURF.fill(BLACK)
        mid.draw(RED,dispSURF)
        snack.draw(GREY,dispSURF)
        snack2.draw(GREY,dispSURF)
        pygame.display.update()
        fpsClock.tick(FPS)

main()
