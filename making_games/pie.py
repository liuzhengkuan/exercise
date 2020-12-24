import math
import pygame,sys
from pygame.locals import *
white = 255, 255, 255
blue = 0, 0, 255
pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60) 
color = 200,80,60
width = 4
x = 300
y = 250
radius =200
position = x - radius, y - radius, radius * 2, radius * 2

piece1 = False
piece2 = False
piece3 = False
piece4 = False

while True:
    for event in pygame.event.get():
        if event.type in QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
                
    screen.fill(blue)
    screen.blit(textImage,(100,100))
    pygame.display.update()
