import contextlib
with contextlib.redirect_stdout(None): import pygame

color = pygame.Color(0, 0, 0, 255)
width = 10
height = 10

class Robber(pygame.sprite.Sprite):

	# Constructor. Pass in the color of the block,
	# and its x and y position
	def __init__(self, x, y):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([width, height])
		self.image.fill(color)

		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.x = x;
		self.y = y;
		self.nextx = x * 10;
		self.nexty = y * 10;
		self.rect.x = x * 10
		self.rect.y = y * 10

	def move(self, robbermap):
		if self.rect.x == self.nextx and self.rect.y == self.nexty:
			x = int(self.nextx / 10)
			y = int(self.nexty / 10)
			robbermap[y][x] = '_'

			if robbermap[y + 1][x] != '_':
				self.nextx = x * 10
				self.nexty = (y + 1) * 10
			elif robbermap[y][x + 1] != '_':
				self.nextx = (x + 1) * 10
				self.nexty = y * 10
			elif robbermap[y - 1][x] != '_':
				self.nextx = x * 10
				self.nexty = (y - 1) * 10
			elif robbermap[y][x - 1] != '_':
				self.nextx = (x - 1) * 10
				self.nexty = y * 10
		else:
			if self.nextx > self.rect.x:
				self.rect.x += 1
			elif self.nextx < self.rect.x:
				self.rect.x -= 1

			if self.nexty > self.rect.y:
				self.rect.y += 1
			elif self.nexty < self.rect.y:
				self.rect.y -= 1

	def getNext(self, robbermap):
		return 10, 10

