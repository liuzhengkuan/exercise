import math
import pygame,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYUP):
            sys.exit()
    screen.fill((0,0,200))

    color=255,0,255
    width=2
    ract=0,0,200,200
    start_angle=math.radians(0)
    end_angle=math.radians(180)
    pygame.draw.arc(screen,color,ract,start_angle,end_angle,width)

    pygame.display.update()