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
		pygame.mixer.music.load("assets/audio/music/Lynx - Espionage.mp3")
		pygame.mixer.music.play(-1)

	def updateSelected(self, event):
		if event.type == pygame.MOUSEMOTION:
			for i in range(len(options)):
				if cxgetRect(options[i], 50, 500 + 80 * i).collidepoint(event.pos):
					self.current = i
		elif event.type == pygame.MOUSEBUTTONDOWN:
			for i in range(len(options)):
				if cxgetRect(options[i], 55, 500 + 80 * i).collidepoint(event.pos):
					return i
		return -2

			

	def update(self, keys_pressed):
		if pygame.K_RETURN in keys_pressed:
			pygame.mixer.music.stop()

			if self.current == 0:
				pygame.mixer.music.load("assets/audio/music/Curie - curious.mp3")
				pygame.mixer.music.play(-1)

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

