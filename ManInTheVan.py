#!/usr/bin/python3

import os
import sys
import time

import contextlib
with contextlib.redirect_stdout(None): import pygame
import pygame.gfxdraw

from LevelLoader import loadLevel
from Robber import Robber
from Camera import Camera

WIDTH = 960
HEIGHT = 960

pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption('Man In The Van')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.display.get_surface()

rx, ry, robbermap1, tilemap1, cameras1, robots1, walls1, floors1 = loadLevel("level1.txt")

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
			for object in cameras1.sprites() + robots1.sprites():
				if object.rect.collidepoint(event.pos):
					selectedRect = pygame.Rect(object.rect.x, object.rect.y, object.width, object.height)
					selected = object
					clickedOnObject = True
				if not clickedOnObject and selected:
					selected = None

	if selected:
		selectedRect.x = selected.rect.x
		selectedRect.y = selected.rect.y 
		selected.update(keys_pressed, tilemap1)
	
	robber.move(robbermap1)

	for object in cameras1.sprites():
		if(object.isSeen((robber.rect.x + robber.rect.width / 2, robber.rect.y + robber.rect.height / 2))):
			print("SEEN!")

	# update and draw
	surface.fill((0, 0, 0))
	floors1.draw(surface)
	robots1.draw(surface)
	robbers.draw(surface)
	for object in cameras1.sprites():
		pygame.gfxdraw.filled_polygon(screen, object.getLightCone(), pygame.Color(247, 238, 69,100))
	cameras1.draw(surface)
	walls1.draw(surface)
	if selected:
		pygame.gfxdraw.rectangle(screen, selectedRect, pygame.Color(255, 0, 0, 100))
	pygame.display.update()

pygame.quit()
sys.exit()
