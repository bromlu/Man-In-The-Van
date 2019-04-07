import contextlib
with contextlib.redirect_stdout(None): import pygame
from Constants import TILE_SIZE
from pygame import Vector2

class Robot(pygame.sprite.Sprite):

	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("assets/rumba-dark-small.png")
		self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

		self.orig_image = self.image
		self.pos = Vector2(pos)  # The original center position/pivot point.
		self.orig_vector = Vector2(pos)
		self.offset = Vector2(0, 0)
		self.rect = self.image.get_rect(center=pos+self.offset)
		self.angle = 0

		self.selectOffset = (0,0)
		self.width = self.rect.width
		self.height = self.rect.height
		self.speed = 10

	def rotate(self):
		self.image = pygame.transform.rotozoom(self.orig_image, -self.angle, 1)
		offset_rotated = self.offset.rotate(self.angle)
		self.rect = self.image.get_rect(center=self.pos+offset_rotated)

	def update1(self):
		self.angle += 30
		self.rotate()

	def update(self, keys_pressed, tilemap):
		if pygame.K_UP in keys_pressed and self.checkBounds(tilemap, self.rect.x, self.rect.y - self.speed):
			self.angle = 0 - 30
			self.rotate()
			self.rect.y -= self.speed
			self.pos.y -= self.speed
		elif pygame.K_RIGHT in keys_pressed and self.checkBounds(tilemap, self.rect.x + self.speed, self.rect.y):
			self.angle = 90 - 30
			self.rotate()
			self.rect.x += self.speed
			self.pos.x += self.speed
		elif pygame.K_DOWN in keys_pressed and self.checkBounds(tilemap, self.rect.x, self.rect.y + self.speed):
			self.angle = 180 - 30
			self.rotate()
			self.rect.y += self.speed
			self.pos.y += self.speed
		elif pygame.K_LEFT in keys_pressed and self.checkBounds(tilemap, self.rect.x - self.speed, self.rect.y):
			self.angle = 270 - 30
			self.rotate()
			self.rect.x -= self.speed
			self.pos.x -= self.speed

	def checkBounds(self, tilemap, x, y):
		x1 = int(x/TILE_SIZE)
		y1  = int(y/TILE_SIZE)
		x2 = int((x + self.width)/TILE_SIZE)
		y2  = int(y/TILE_SIZE)
		x3 = int(x/TILE_SIZE)
		y3  = int((y + self.height)/TILE_SIZE)
		x4 = int((x + self.width)/TILE_SIZE)
		y4  = int((y + self.height)/TILE_SIZE)
		if(int(tilemap[y1][x1]) % 2 == 1 or int(tilemap[y2][x2]) % 2 == 1 or int(tilemap[y3][x3]) % 2 == 1 or int(tilemap[y4][x4]) % 2 == 1):
			return False
		return True

	def reset(self):
		self.offset = Vector2(0, 0)
		self.rect = self.image.get_rect(center=self.orig_vector+self.offset)
		self.rect.x = self.orig_vector.x
		self.rect.y = self.orig_vector.y
		self.pos.x = self.orig_vector.x
		self.pos.y = self.orig_vector.y
		self.angle = 0



