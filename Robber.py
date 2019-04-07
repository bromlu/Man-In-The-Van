import contextlib
with contextlib.redirect_stdout(None): import pygame
from Constants import TILE_SIZE
import time

color = pygame.Color(0, 0, 0, 255)
width = TILE_SIZE
height = TILE_SIZE
scale = 2

class Robber(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.spriteSheetDown = pygame.image.load("assets/ninja-down.png").convert_alpha()
		self.spriteSheetLeft = pygame.image.load("assets/ninja-left.png").convert_alpha()
		self.spriteSheetRight = pygame.image.load("assets/ninja-right.png").convert_alpha()
		self.spriteSheetUp = pygame.image.load("assets/ninja-up.png").convert_alpha()
		self.spriteSheetDown = pygame.transform.scale(self.spriteSheetDown, (24*8*scale, 32*scale))
		self.spriteSheetLeft = pygame.transform.scale(self.spriteSheetLeft, (24*8*scale, 32*scale))
		self.spriteSheetRight = pygame.transform.scale(self.spriteSheetRight, (24*8*scale, 32*scale))
		self.spriteSheetUp = pygame.transform.scale(self.spriteSheetUp, (24*8*scale, 32*scale))

		self.image = pygame.Surface((24 * scale, 32 * scale)).convert()
		self.image.fill((100,100,100))
		self.image.set_colorkey((100, 100, 100))
		self.image.blit(self.spriteSheetRight, (0,0), (24 * scale,32 * scale,24 * scale,32 * scale))


		self.animations = [
			(0 * scale, 0, 24 * scale, 32 * scale),
			(24 * scale, 0, 24 * scale, 32 * scale),
			(48 * scale, 0, 24 * scale, 32 * scale),
			(72 * scale, 0, 24 * scale, 32 * scale),
			(96 * scale, 0, 24 * scale, 32 * scale),
			(120 * scale, 0, 24 * scale, 32 * scale),
			(144 * scale, 0, 24 * scale, 32 * scale),
			(168 * scale, 0, 24 * scale, 32 * scale),
		]

		self.animationIndex = 0
		self.animationSpeed = 1.0/8.0
		self.last = 0
		self.speed = 2

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
				self.rect.x += self.speed
				self.walkRight()
			elif self.nextx < self.rect.x:
				self.rect.x -= self.speed
				self.walkLeft()
			if self.nexty > self.rect.y:
				self.rect.y += self.speed
				self.walkDown()
			elif self.nexty < self.rect.y:
				self.rect.y -= self.speed
				self.walkUp()

	def walkRight(self):
		if time.time() - self.last < self.animationSpeed: return
		self.last = time.time()
		self.image.fill((100,100,100))
		self.image.blit(self.spriteSheetRight, (0,0), self.animations[self.animationIndex])
		self.animationIndex += 1
		self.animationIndex = self.animationIndex % 7

	def walkDown(self):
		if time.time() - self.last < self.animationSpeed: return
		self.last = time.time()
		self.image.fill((100,100,100))
		self.image.blit(self.spriteSheetDown, (0,0), self.animations[self.animationIndex])
		self.animationIndex += 1
		self.animationIndex = self.animationIndex % 7

	def walkLeft(self):
		if time.time() - self.last < self.animationSpeed: return
		self.last = time.time()
		self.image.fill((100,100,100))
		self.image.blit(self.spriteSheetLeft, (0,0), self.animations[self.animationIndex])
		self.animationIndex += 1
		self.animationIndex = self.animationIndex % 7

	def walkUp(self):
		if time.time() - self.last < self.animationSpeed: return
		self.last = time.time()
		self.image.fill((100,100,100))
		self.image.blit(self.spriteSheetUp, (0,0), self.animations[self.animationIndex])
		self.animationIndex += 1
		self.animationIndex = self.animationIndex % 7
