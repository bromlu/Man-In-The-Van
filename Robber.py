import contextlib
with contextlib.redirect_stdout(None): import pygame

color = pygame.Color(0, 0, 0, 255)
width = 50
height = 50

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
		self.x = x
		self.y = y
		self.nextx = x * 50
		self.nexty = y * 50
		self.rect.x = x * 50
		self.rect.y = y * 50

	def move(self, robbermap):
		if self.rect.x == self.nextx and self.rect.y == self.nexty:
			x = int(self.nextx / 50)
			y = int(self.nexty / 50)
			robbermap[y][x] = '_'

			if robbermap[y + 1][x] == 'R':
				self.nextx = x * 50
				self.nexty = (y + 1) * 50
			elif robbermap[y][x + 1] == 'R':
				self.nextx = (x + 1) * 50
				self.nexty = y * 50
			elif robbermap[y - 1][x] == 'R':
				self.nextx = x * 50
				self.nexty = (y - 1) * 50
			elif robbermap[y][x - 1] == 'R':
				self.nextx = (x - 1) * 50
				self.nexty = y * 50
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
		return 50, 50

