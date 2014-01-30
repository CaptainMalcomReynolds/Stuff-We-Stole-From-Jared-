import pygame
import graphics
import game
from sprite import Sprite

import random

for i in range(100):
    random.seed(random.randint(1,10000000000))

colors=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
accels=[0,0,0]

sizes=[random.randint(10,1280),random.randint(10,720)]
accels1=[0,0]

interval=1
interval2=5

maxint=5
maxint2=25

def solve(num):
    i=colors[num]
    v=accels[num]
    colors[num]+=v
    if colors[num]>255:
        colors[num]=255
    elif colors[num]<0:
        colors[num]=0
    accels[num]+=random.randint(-interval,interval)
    if accels[num]>maxint:
        accels[num]=maxint
    elif accels[num]<-maxint:
        accels[num]=-maxint

def solve2(num,min1,max1):
    i=sizes[num]
    v=accels1[num]
    sizes[num]+=v
    if sizes[num]>max1:
        sizes[num]=max1
    elif sizes[num]<min1:
        sizes[num]=min1
    accels1[num]+=random.randint(-interval2,interval2)
    if accels1[num]>maxint2:
        accels1[num]=maxint2
    elif accels1[num]<-maxint2:
        accels1[num]=-maxint2

def draw():
    """
    Drawing logic
    """

    # Fill the screen with black
    solve(0)
    solve(1)
    solve(2)
    solve2(0,10,1280)
    solve2(1,10,720)
    # game.screen = pygame.display.set_mode((sizes[0],sizes[1]),pygame.DOUBLEBUF)
    background = pygame.Surface(game.screen.get_size())
    background = background.convert()
    game.screen.blit(background,(0,0))
    game.screen.fill((colors[0],colors[1],colors[2]))
    
    # insert logic here

    # Don't change these
    pygame.display.update()
    pygame.display.flip()

    return