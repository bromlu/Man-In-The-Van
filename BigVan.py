import contextlib
with contextlib.redirect_stdout(None): import pygame
from Constants import TILE_SIZE
import time

color = pygame.Color(0, 0, 0, 255)
width = TILE_SIZE
height = TILE_SIZE
scale = 30

class BigVan(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.bigVan = pygame.image.load("assets/white-van.png").convert_alpha()
		self.bigVan = pygame.transform.scale(self.bigVan, (16*scale, 16*scale))

		self.image = pygame.Surface((16 * scale, 16 * scale)).convert()
		self.image.fill((100,100,100))
		self.image.set_colorkey((100, 100, 100))
		self.image.blit(self.bigVan, (0,0), (0,0,16 * scale,16 * scale))

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y 