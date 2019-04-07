#!/usr/bin/python3

import os
import sys
import time

import contextlib
with contextlib.redirect_stdout(None): import pygame
import pygame.gfxdraw
import math

from Constants import *
from Menu import Menu
from Game import Game
from Transition import Transition

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

levels = [
	Transition(["Alright this is it. As soon as I get in there we won’t have much time before you get logged out, and we know how you are with passwords. So... I’m gonna try to get to the safe as fast as possible. Do you have control of the cameras?",
	"You’re gonna do great, it’s all easy stuff. I’m sure you can figure it out but I’ll give you a quick rundown: select the cameras and other hacked tech and then use the arrow keys to move them out of the way.",
	"Ok, just don’t let me get caught on camera, or like hit with a rumba or something. Haha. Ready?",
	"Good. Keep the engine running."
]),
	Game("level1.txt"),
	Game("level2.txt"),
	Game("level3.txt"),
	Game("level4.txt"),
	Game("level5.txt"),
]
levelIndex = -1

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
		print(levelIndex)
		levelIndex += 1
		levelIndex % 5
		level = levels[levelIndex]
	elif state == 1:
		done = True
	

	surface.fill((0, 0, 0))
	level.draw(screen, surface)
	pygame.display.update()

pygame.quit()
sys.exit()
