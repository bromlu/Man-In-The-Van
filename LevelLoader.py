import contextlib
with contextlib.redirect_stdout(None): import pygame

from Tiles import WallTile, FloorTile
from Camera import Camera

def loadLevel(levelText):
	file = open(levelText, "r" )
	data = file.read().replace("\n", "").replace("  ", " ").split(" ")
	file.close()
	map = pygame.sprite.Group()
	objects = pygame.sprite.Group()
	tile = None
	for i in range(len(data)):
		x = (i % 24) * 10
		y = int(i / 24) * 10
		if data[i] == "W" or data[i] == "CW":
			tile = WallTile()
		if data[i] == "CW":
			camera = Camera()
			camera.rect.x = x
			camera.rect.y = y
			objects.add(camera)
		if data[i] == "F" or data[i] == "RF":
			tile = FloorTile()
		tile.rect.x = x
		tile.rect.y = y
		map.add(tile)

	return map, objects