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

		self.rect = self.image.get_rect()
		self.rect.x = origin[0]
		self.rect.y = origin[1]
		print(self.rect.x)

