#!/usr/bin/python3

import os
import sys
import time

import contextlib
with contextlib.redirect_stdout(None): import pygame
import pygame.gfxdraw

from Font import *
from Constants import *
from BigRobber import BigRobber

options = ["Play", "Quit"]
white = pygame.Color(255, 255, 255, 255)

class Transition():
	def __init__(self, dialog):
		self.current = 0		
		self.dialog = dialog	
		self.robbers = pygame.sprite.Group()
		self.robbers.add(BigRobber(0,HEIGHT/3))

	def update(self, keys_pressed):
		if pygame.K_RETURN in keys_pressed:
			self.current += 1
			print(self.current)
			print(len(self.dialog))
			if self.current >= len(self.dialog):
				print("AHHH")
				return 0
		return -2

	def draw(self, screen, surface):
		cxprint(screen, surface, "Press Enter to continue", 80, white, HEIGHT-80)
		self.drawDialogBox(screen, self.dialog[self.current], 200, 200)
		self.robbers.draw(surface)

	def drawDialogBox(self, screen, string, x, y):
		size = 24
		maxWidth = WIDTH/4*5
		yOffset = 0
		length = len(string) * size
		height = int(max(length/maxWidth * (size + 5), size+5))
		width = int(min(length, maxWidth))
		pygame.gfxdraw.filled_ellipse(screen, int(x + width/4), int(y + height), int(width/3), height*2, pygame.Color(255, 255, 255, 255))
		while length > maxWidth:
			breakPoint = string.find(' ', int(maxWidth/size))
			newString = string[:breakPoint]
			string = string[breakPoint:]
			yOffset += size + 5
			tlprint(screen, newString, size, pygame.Color(0,0,0), x, y + yOffset)
			length = len(string) * size
		yOffset += size
		tlprint(screen, string, size, pygame.Color(0,0,0), x, y + yOffset)

