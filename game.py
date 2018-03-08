#!/usr/bin/python

import pygame, sys, numpy, time
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
snack = character.Character(numpy.random.randint(0,DISP_WIDTH),numpy.random.randint(150,DISP_HEIGHT))
snack2= character.Character(numpy.random.randint(0,DISP_WIDTH),numpy.random.randint(150,DISP_HEIGHT))


fpsClock=pygame.time.Clock()

dispSURF=pygame.display.set_mode((DISP_WIDTH,DISP_HEIGHT),0,32)


def disp_text(score,surf,size,x,y,color):
    scoreObj = pygame.font.Font('freesansbold.ttf', size)  #font obj
    scoreSurfaceObj = scoreObj.render(str(score), True, color)
    scoreRectObj = scoreSurfaceObj.get_rect() #text box
    scoreRectObj.center = (x, y) #text box center
    dispSURF.blit(scoreSurfaceObj,scoreRectObj)

                  

def draw_world(surf): #draws everything for scenery
    surf.fill(BLACK) #fills black background
    fontObj = pygame.font.Font('freesansbold.ttf', 32)  #font obj
    textSurfaceObj = fontObj.render('Score: ', True, WHITE)
    textRectObj = textSurfaceObj.get_rect() #text box
    textRectObj.center = (100, 25) #text box center
    surf.blit(textSurfaceObj, textRectObj) #puts text to screen


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
            
                        
        draw_world(dispSURF)
        disp_text(str(score),dispSURF,32,250,25,WHITE)
        if score==10:
            disp_text("You win!",dispSURF,32,150,50,WHITE)
            time.sleep(3)
            break
        mid.draw(RED,dispSURF)
        snack.draw(GREY,dispSURF)
        snack2.draw(GREY,dispSURF)
        pygame.display.update()
        fpsClock.tick(FPS)

main()
