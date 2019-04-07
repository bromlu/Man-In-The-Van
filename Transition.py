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
from BigVan import BigVan

options = ["Play", "Quit"]
white = pygame.Color(255, 255, 255, 255)

class Transition():
	def __init__(self, dialog, isVan, driving=False):
		self.pause = 10
		self.paused = True
		self.driving = driving
		self.current = 0		
		self.dialog = dialog	
		self.sprites = pygame.sprite.Group()
		if not isVan:
			self.sprites.add(BigRobber(0,HEIGHT/3))
		else:
			self.sprites.add(BigVan(0,HEIGHT/3+ 50))

	def updateSelected(self, event):
		return -2

	def update(self, keys_pressed):
		if self.current >= len(self.dialog):
			self.current = 0
		if self.driving:
			self.sprites.sprites()[0].rect.x += 5
		if pygame.K_RETURN in keys_pressed:

			if self.paused:
				self.pause -= 1
			if self.pause < 0:
				self.paused = False
		
			jump = False
			if not self.paused:
				jump = True
				self.pause = 10
			elif self.pause <= 0:
				jump = True
				self.pause = 10

			if jump:
				self.current += 1
				if self.current >= len(self.dialog):
					return 0
		return -2

	def draw(self, screen, surface):
		if self.current >= len(self.dialog):
			return
		cxprint(screen, surface, "Press Enter to continue", 80, white, HEIGHT-80)
		self.drawDialogBox(screen, self.dialog[self.current], 200, 200)
		self.sprites.draw(surface)

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

