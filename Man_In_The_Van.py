#!/usr/bin/python3

import os
import sys
import time

import contextlib
with contextlib.redirect_stdout(None): import pygame

from LevelLoader import loadLevel
from Robber import Robber

WIDTH = 1200
HEIGHT = 800

pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption('Man In The Van')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.display.get_surface()




last = 0
robber = Robber(pygame.Color(255, 255, 255, 0), 20, 20)
robber.rect.x = 10
robber.rect.y = 10
robbers = pygame.sprite.Group()
robbers.add(robber)

level1 = loadLevel("level1.txt")




keys_pressed = set()
done = False
while not done:
    # delay until 1/60th of second
    while time.time() - last < 1/60: pass
    last = time.time()


    # pump events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            keys_pressed.add(event.key)
        if event.type == pygame.KEYUP:
            keys_pressed.remove(event.key)

    # update and draw
    surface.fill((0, 0, 0))
    robbers.draw(surface)
    level1.draw(surface)
    pygame.display.update()

pygame.quit()
sys.exit()