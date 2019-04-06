import contextlib
with contextlib.redirect_stdout(None): import pygame

from Constants import TILE_SIZE

def getFilename(tile):
	filename = ''
	if tile == 0 or tile == 1:
		filename = 'dark-marble.png'
	elif tile == 2 or tile == 3:
		filename = 'earth.png'
	elif tile == 4 or tile == 5:
		filename = 'fancy-tile.png'
	elif tile == 6 or tile == 7:
		filename = 'light-marble.png'
	elif tile == 8 or tile == 9:
		filename = 'wood-tile.png'
	elif tile == 10 or tile == 11:
		filename = 'wood-tile-2.png'

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

