#!/usr/bin/python3

import os
import sys
import time

import contextlib
with contextlib.redirect_stdout(None): import pygame

from Robber import Robber

WIDTH = 1200
HEIGHT = 800

pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption('Man In The Van')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.display.get_surface()

keys_pressed = set()
done = False
last = 0
robber = Robber(pygame.Color(255, 255, 255, 0), 200, 200)
robber.rect.x = 10
robber.rect.y = 10
group = pygame.sprite.Group()
group.add(robber)

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
    group.draw(surface)
    pygame.display.update()

pygame.quit()
sys.exit()