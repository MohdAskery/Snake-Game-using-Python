import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,500))

bg = pygame.image.load("img.jpeg")


pygame.mouse.set_visible(0)



pygame.display.set_caption('galaxy invaders')

while True:
    clock.tick(60)
    screen.fill((0,0,0))
    screen.blit(bg(0,0))