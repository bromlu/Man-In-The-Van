#!/usr/bin/python3

import os
import sys
import time

import contextlib
with contextlib.redirect_stdout(None): import pygame
import pygame.gfxdraw
import math

from Menu import Menu
from Game import Game

WIDTH = 960
HEIGHT = 960

pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption('Man In The Van')
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.display.get_surface()

last = 0
keys_pressed = set()
done = False
level = Menu()

while not done:
	state = -2
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
		if event.type == pygame.MOUSEMOTION:
			state = level.updateSelected(event)
		if event.type == pygame.MOUSEBUTTONDOWN:
			state = level.updateSelected(event)
	
	if state == -2:
		state = level.update(keys_pressed)
	if state == -1:
		level = Menu()
	elif state == 0:
		level = Game("level1.txt")
	elif state == 1:
		done = True
	

	surface.fill((0, 0, 0))
	level.draw(screen, surface)
	pygame.display.update()

pygame.quit()
sys.exit()
