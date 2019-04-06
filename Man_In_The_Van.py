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

rx, ry, robbermap1, tilemap1, spritemap1, objectmap1 = loadLevel("level1.txt")

robber = Robber(rx, ry)
robbers = pygame.sprite.Group()
robbers.add(robber)

selected = None
last = 0
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
		if event.type == pygame.MOUSEBUTTONDOWN:
			clickedOnObject = False
			for object in objectmap1.sprites():
				if object.rect.collidepoint(event.pos):
					selectedRect = pygame.Rect(object.rect.x, object.rect.y, object.width, object.height)
					selected = object
					clickedOnObject = True
				if not clickedOnObject and selected:
					selected = None

	if selected:
		selected.update(keys_pressed, tilemap1)
	
	robber.move(robbermap1)

	# update and draw
	surface.fill((0, 0, 0))
	spritemap1.draw(surface)
	objectmap1.draw(surface)
	robbers.draw(surface)
	if selected:
		see_through = pygame.Surface((selectedRect.width,selectedRect.height)).convert_alpha()
		see_through.fill(pygame.Color(255, 0, 0, 20))
		screen.blit(see_through, selectedRect)
	pygame.display.update()

pygame.quit()
sys.exit()
