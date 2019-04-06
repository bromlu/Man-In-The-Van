import contextlib
with contextlib.redirect_stdout(None): import pygame

from Tiles import WallTile, FloorTile

width = 24
height = 24

def loadLevel(levelText):
	file = open(levelText, "r" )
	data = file.read().replace("\n", " ").split(" ")
	file.close()

	robbermap = []
	rx = 0;
	ry = 0;
	tilemap = []
	spritemap = pygame.sprite.Group()
	
	tile = None
	for i in range(len(data) - 1):
		col = i % width
		row = int(i / width);
		if(row == 0):
			robbermap.append([]);
			tilemap.append([]);

		robbermap[row].append(data[i][0])
		if(data[i][0] == 'S'):
			rx = col
			ry = row
		tilemap[row].append(data[i][1])

		if data[i][1] == 'W':
			tile = WallTile()
		elif data[i][1] == 'F':
			tile = FloorTile()
		tile.rect.x = col * 10
		tile.rect.y = row * 10
		spritemap.add(tile)

	robbermap[ry][rx] = '_'

	return rx, ry, robbermap, tilemap, spritemap
