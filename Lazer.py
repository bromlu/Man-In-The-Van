import contextlib
with contextlib.redirect_stdout(None): import pygame

from math import *
from Constants import TILE_SIZE

class Lazer(pygame.sprite.Sprite):
	def __init__(self, origin, height, width):
		pygame.sprite.Sprite.__init__(self)

		print(origin, height, width)

		self.image = pygame.Surface([height, width]).convert_alpha()
		self.image.fill(pygame.Color(255,0,0, 50))

		self.original_image = self.image
		self.rect = self.image.get_rect()
		self.rect.x = origin[0]
		self.rect.y = origin[1]
		print(self.rect.x)

	def block(self, pos):
		width = self.rect.width
		height = self.rect.height
		if width <= TILE_SIZE/8:
			dif = abs(self.rect.y - pos.y)
			height = dif
		else:
			dif = abs(self.rect.x - pos.x)
			width = dif
		if width == 0: width = 1
		if height == 0: height = 1
		self.image = pygame.Surface([width, height]).convert_alpha()
		self.image.fill(pygame.Color(255,0,0, 50))
		x = self.rect.x
		y = self.rect.y
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def reset(self):
		self.image = self.original_image
		x = self.rect.x
		y = self.rect.y
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y 


