#!/usr/bin/python3

import os
import sys
import time

import contextlib
with contextlib.redirect_stdout(None): import pygame
import pygame.gfxdraw

from Font import *

options = ["Play", "Quit"]
white = pygame.Color(255, 255, 255, 255)



class Menu():
	def __init__(self):
		self.current = 0
		self.pause = 0
		self.paused = False

	def updateSelected(self, event):
#		clickedOnObject = False
#		for object in self.cameras.sprites() + self.robots.sprites():
#			if object.rect.collidepoint(event.pos):
#				self.selectedRect = pygame.Rect(object.rect.x, object.rect.y, object.width, object.height)
#				self.selected = object
#				clickedOnObject = True
#			if not clickedOnObject and self.selected:
#				self.selected = True
		pass

	def update(self, keys_pressed):
		if pygame.K_RETURN in keys_pressed:
			return self.current

		if self.paused:
			self.pause -= 1
			if self.pause < 0:
				self.paused = False

		if not (pygame.K_UP in keys_pressed or pygame.K_DOWN in keys_pressed or pygame.K_w in keys_pressed or pygame.K_s in keys_pressed):
			self.paused = False
			self.pause = 0
		else:
			jump = False
			if not self.paused:
				jump = True
				self.pause = 30
			elif self.pause <= 0:
				jump = True
				self.pause = 10

			if jump:
				if pygame.K_UP in keys_pressed or pygame.K_w in keys_pressed:
					self.current -= 1
				if pygame.K_DOWN in keys_pressed or pygame.K_s in keys_pressed:
					self.current += 1

				self.current = wrap(self.current, 0, len(options) - 1)
				self.paused = True
		return -2

	def draw(self, screen, surface):
		cxprint(screen, surface, "Man In the Van", 80, white, 300)

		for i in range(len(options)):
			if self.current == i:
				cxprint(screen, surface, options[i], 55, white, 500 + 80 * i)
			else:
				cxprint(screen, surface, options[i], 50, pygame.Color(200, 200, 200, 255), 500 + 80 * i)

