#!/usr/bin/python3

import os
import sys
import time
import copy

import contextlib
with contextlib.redirect_stdout(None): import pygame
import pygame.gfxdraw

from LevelLoader import loadLevel
from Robber import Robber
from Camera import Camera
from Font import *
from Constants import *



class Game():
	def __init__(self, level):
		self.rx, self.ry, self.robbermap, self.tilemap, self.cameras, self.robots, self.walls, self.floors, self.lazers = loadLevel(level)

		self.orig_robbermap = copy.deepcopy(self.robbermap)
		self.robber = Robber(self.rx, self.ry)
		self.robbers = pygame.sprite.Group()
		self.robbers.add(self.robber)

		self.selected = None
		self.selectedRect = None

	def updateSelected(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			clickedOnObject = False
			for object in self.cameras.sprites() + self.robots.sprites():
				if object.rect.collidepoint(event.pos):
					self.selectedRect = pygame.Rect(object.rect.x, object.rect.y, object.width, object.height)
					self.selected = object
					clickedOnObject = True
				if not clickedOnObject and self.selected:
					self.selected = None
		return -2

	def update(self, keys_pressed):
		if self.selected:
			self.selectedRect.x = self.selected.rect.x
			self.selectedRect.y = self.selected.rect.y
			self.selected.update(keys_pressed, self.tilemap)

		finished = self.robber.move(self.robbermap)
		if finished:
			return 0
		return -2

	def draw(self, screen, surface):
		self.floors.draw(surface)
		self.robots.draw(surface)
		self.robbers.draw(surface)
		self.lazers.draw(surface)
		
		for object in self.cameras.sprites():
			if not object.isSeen((self.robber.rect.x + self.robber.rect.width / 2, self.robber.rect.y + self.robber.rect.height /2)):
				pygame.gfxdraw.filled_polygon(screen, object.getLightCone(), pygame.Color(89, 211, 255, 50))
			else:
				pygame.gfxdraw.filled_polygon(screen, object.getLightCone(), pygame.Color(180, 0, 0, 50))
				self.reset()
		self.cameras.draw(surface)
		self.walls.draw(surface)
		
		if self.selected:
			pygame.gfxdraw.rectangle(screen, self.selectedRect, pygame.Color(255, 100, 16, 100))

		if pygame.sprite.groupcollide(self.robbers, self.lazers, False, False):
			self.reset()

		if pygame.sprite.groupcollide(self.robbers, self.robots, False, False):
			self.reset()
		# self.drawDialogBox(screen, "Hey there! imani how are you doing today are you enjoying gamejam? I sure am i miss tim though ey there! imani how are you doing today are you enjoying gamejam? I sure am i miss tim though", 200, 200)
		
		for lazer in self.lazers.sprites():
			collidingRobots = pygame.sprite.spritecollide(lazer, self.robots, False)
			for robot in collidingRobots:
				lazer.block(robot.pos)
			if len(collidingRobots) == 0:
				lazer.reset()
		
		for robot in self.robots.sprites():
			robot.update1()

	def reset(self):
		self.robbermap = copy.deepcopy(self.orig_robbermap)
		self.robber.rect.x = self.rx * TILE_SIZE
		self.robber.rect.y = self.ry * TILE_SIZE
		self.robber.nextx = self.rx * TILE_SIZE
		self.robber.nexty = self.ry * TILE_SIZE
		for robot in self.robots:
			robot.reset()
		for camera in self.cameras:
			camera.reset()

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

