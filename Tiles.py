import contextlib
with contextlib.redirect_stdout(None): import pygame

from Constants import TILE_SIZE

def getFilename(tile):
	filename = ''
	if tile == 0 or tile == 1:
		filename = 'small-black-dirt.png'
	elif tile == 2 or tile == 3:
		filename = 'earth.png'
	elif tile == 4 or tile == 5:
		filename = 'fancy-tile.png'
	elif tile == 6 or tile == 7:
		filename = 'small-tan-marble-2.png'
	elif tile == 8 or tile == 9:
		filename = 'wood-tile.png'
	elif tile == 10 or tile == 11:
		filename = 'wood-tile-2.png'
	elif tile == 12 or tile == 13:
		filename = 'small-blue-carpet.png'
	elif tile == 14 or tile == 15:
		filename = 'fern.png'
	elif tile == 16 or tile == 17:
		filename = 'small-black-marble.png'
	elif tile == 18 or tile == 19:
		filename = 'purple-jewel.png'
	elif tile == 20 or tile == 21:
		filename = 'pink-chair.png'

	return 'assets/' + filename

class WallTile(pygame.sprite.Sprite):
	def __init__(self, pos, tile):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(getFilename(tile))
		self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

class FloorTile(pygame.sprite.Sprite):
	def __init__(self, pos, tile):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(getFilename(tile))
		self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

