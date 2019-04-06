import contextlib
with contextlib.redirect_stdout(None): import pygame
from Constants import TILE_SIZE

color = pygame.Color(0, 0, 0, 255)
width = TILE_SIZE
height = TILE_SIZE
scale = 4

class Robber(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.spriteSheet = pygame.image.load("assets/ninja.png").convert_alpha()
		self.spriteSheet = pygame.transform.scale(self.spriteSheet, (24*8*scale, 32*4*scale))

		self.image = pygame.Surface((24 * scale, 32 * scale)).convert()
		self.image.fill((100,100,100))
		self.image.set_colorkey((100, 100, 100))
		self.image.blit(self.spriteSheet, (0,0), (24 * scale,32 * scale,24 * scale,32 * scale))

		self.downAnimations = [
			(24 * scale,64 * scale,24 * scale,32 * scale),
			(48 * scale,64 * scale,24 * scale,32 * scale),
			(72 * scale,64 * scale,24 * scale,32 * scale),
			(96 * scale,64 * scale,24 * scale,32 * scale),
			(120 * scale,64 * scale,24 * scale,32 * scale),
			(144 * scale,64 * scale,24 * scale,32 * scale),
			(168 * scale,64 * scale,24 * scale,32 * scale),
			(192 * scale,64 * scale,24 * scale,32 * scale),
		]

		self.rightAnimations = [
			(24 * scale,32 * scale,24 * scale,32 * scale),
			(48 * scale,32 * scale,24 * scale,32 * scale),
			(72 * scale,32 * scale,24 * scale,32 * scale),
			(96 * scale,32 * scale,24 * scale,32 * scale),
			(120 * scale,32 * scale,24 * scale,32 * scale),
			(144 * scale,32 * scale,24 * scale,32 * scale),
			(168 * scale,32 * scale,24 * scale,32 * scale),
			(192 * scale,32 * scale,24 * scale,32 * scale),
		]

		self.upAnimations = [
			(24 * scale,0 * scale,24 * scale,32 * scale),
			(48 * scale,0 * scale,24 * scale,32 * scale),
			(72 * scale,0 * scale,24 * scale,32 * scale),
			(96 * scale,0 * scale,24 * scale,32 * scale),
			(120 * scale,0 * scale,24 * scale,32 * scale),
			(144 * scale,0 * scale,24 * scale,32 * scale),
			(168 * scale,0 * scale,24 * scale,32 * scale),
			(192 * scale,0 * scale,24 * scale,32 * scale),
		]

		self.leftAnimations = [
			(24 * scale,96 * scale,24 * scale,32 * scale),
			(48 * scale,96 * scale,24 * scale,32 * scale),
			(72 * scale,96 * scale,24 * scale,32 * scale),
			(96 * scale,96 * scale,24 * scale,32 * scale),
			(120 * scale,96 * scale,24 * scale,32 * scale),
			(144 * scale,96 * scale,24 * scale,32 * scale),
			(168 * scale,96 * scale,24 * scale,32 * scale),
			(192 * scale,96 * scale,24 * scale,32 * scale),
		]

		self.animationIndex = 0

		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.nextx = x * TILE_SIZE
		self.nexty = y * TILE_SIZE
		self.rect.x = x * TILE_SIZE
		self.rect.y = y * TILE_SIZE

	def move(self, robbermap):
		if self.rect.x == self.nextx and self.rect.y == self.nexty:
			x = int(self.nextx / TILE_SIZE)
			y = int(self.nexty / TILE_SIZE)
			robbermap[y][x] = '_'

			if robbermap[y + 1][x] == 'R':
				self.nextx = x * TILE_SIZE
				self.nexty = (y + 1) * TILE_SIZE
			elif robbermap[y][x + 1] == 'R':
				self.nextx = (x + 1) * TILE_SIZE
				self.nexty = y * TILE_SIZE
			elif robbermap[y - 1][x] == 'R':
				self.nextx = x * TILE_SIZE
				self.nexty = (y - 1) * TILE_SIZE
			elif robbermap[y][x - 1] == 'R':
				self.nextx = (x - 1) * TILE_SIZE
				self.nexty = y * TILE_SIZE
		else:
			if self.nextx > self.rect.x:
				self.rect.x += 5
				self.walkRight()
			elif self.nextx < self.rect.x:
				self.rect.x -= 5

			if self.nexty > self.rect.y:
				self.rect.y += 5
				self.walkDown()
			elif self.nexty < self.rect.y:
				self.rect.y -= 5

	def walkRight(self):
		self.image.fill((100,100,100))
		self.image.blit(self.spriteSheet, (0,0), self.rightAnimations[self.animationIndex])
		self.animationIndex += 1
		self.animationIndex = self.animationIndex % 7

	def walkDown(self):
		self.image.fill((100,100,100))
		self.image.blit(self.spriteSheet, (0,0), self.downAnimations[self.animationIndex])
		self.animationIndex += 1
		self.animationIndex = self.animationIndex % 7
