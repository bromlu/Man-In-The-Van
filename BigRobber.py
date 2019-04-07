import contextlib
with contextlib.redirect_stdout(None): import pygame
from Constants import TILE_SIZE
import time

color = pygame.Color(0, 0, 0, 255)
width = TILE_SIZE
height = TILE_SIZE
scale = 14

class BigRobber(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.spriteSheet = pygame.image.load("assets/ninja-down.png").convert_alpha()
		self.spriteSheet = pygame.transform.scale(self.spriteSheet, (24*8*scale, 32*scale))

		self.image = pygame.Surface((24 * scale, 32 * scale)).convert()
		self.image.fill((100,100,100))
		self.image.set_colorkey((100, 100, 100))
		self.image.blit(self.spriteSheet, (0,0), (0,0,24 * scale,32 * scale))

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y 