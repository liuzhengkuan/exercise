import pygame,sys
from pygame.locals import *
pygame.init()
screen = 600,500
mydisp = pygame.display.set_mode(screen)
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    mydisp.fill((0,80,0))
    color =100,255,200
    width = 8
    pygame.draw.line(mydisp,color,(100,100),(500,400),width)
    pygame.display.update()
