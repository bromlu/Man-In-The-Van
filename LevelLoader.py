import contextlib
with contextlib.redirect_stdout(None): import pygame

from Tiles import WallTile, FloorTile
from Camera import Camera
from Robot import Robot
from Constants import TILE_SIZE

width = 24
height = 24

def makeCamera(data, i, col, row):
	walls = [
		data[i-width-1][1] == 'W',
		data[i-width][1] == 'W',
		data[i-width+1][1] == 'W',
		data[i-1][1] == 'W',
		False,
		data[i+1][1] == 'W',
		data[i+width-1][1] == 'W',
		data[i+width][1] == 'W',
		data[i+width+1][1] == 'W',
	]

	rotation = 0
	range = 0 
	offset = (0, 0)
	multiplier = 1

	if(walls[1] and not walls[3] and not walls[5]):
		rotation = 90
		range = 180
	elif(walls[3] and not walls[1] and not walls[7]):
		rotation = 0
		range = 180
	elif(walls[5] and not walls[1] and not walls[7]):
		rotation = 180
		range = 180
		offset = (TILE_SIZE, 0)
		multiplier = -1
	elif(walls[7] and not walls[3] and not walls[5]):
		rotation = 270
		range = 180
		offset = (0, TILE_SIZE)
		multiplier = -1

	if(walls[0] and not walls[1] and not walls[3]):
		rotation = 45
		range = 270
	elif(walls[2] and not walls[1] and not walls[5]):
		rotation = 135
		range = 270
		offset = (TILE_SIZE, 0)
	elif(walls[6] and not walls[3] and not walls[7]):
		rotation = 315
		range = 270
		offset = (0, TILE_SIZE)
		multiplier = -1
	elif(walls[8] and not walls[5] and not walls[7]):
		multiplier = -1
		rotation = 225
		range = 270
		offset = (TILE_SIZE, TILE_SIZE)

	if(walls[0] and walls[1] and walls[3]):
		rotation = 45
		range = 90
	elif(walls[2] and walls[1] and walls[5]):
		rotation = 135
		range = 90
		offset = (TILE_SIZE, 0)
	elif(walls[6] and walls[3] and walls[7]):
		rotation = 315
		range = 90
		offset = (0, TILE_SIZE)
		multiplier = -1
	elif(walls[8] and walls[5] and walls[7]):
		rotation = 225
		range = 90
		offset = (TILE_SIZE, TILE_SIZE)
		multiplier = -1

	return Camera((col * TILE_SIZE + offset[0], row * TILE_SIZE + offset[1]), rotation, rotation - range/2, rotation + range/2, multiplier, offset)

def loadLevel(levelText):
	file = open(levelText, "r" )
	data = file.read().replace("\n", " ").split(" ")
	file.close()

	robbermap = []
	rx = 0
	ry = 0
	tilemap = []
	floors = pygame.sprite.Group()
	cameras = pygame.sprite.Group()
	robots = pygame.sprite.Group()
	walls = pygame.sprite.Group()
	
	tile = None
	for i in range(len(data) - 1):
		col = i % width
		row = int(i / width)
		if(row == 0):
			robbermap.append([])
			tilemap.append([])

		robbermap[row].append(data[i][0])
		if(data[i][0] == 'S'):
			rx = col
			ry = row
		tilemap[row].append(data[i][1])

		if(data[i][0] == 'C'):
			cameras.add(makeCamera(data, i, col, row))
		if(data[i][0] == 'M'):
			robot = Robot((col * TILE_SIZE, row * TILE_SIZE))
			robots.add(robot)
			pass

		if data[i][1] == 'W':
			tile = WallTile()
			tile.rect.x = col * TILE_SIZE
			tile.rect.y = row * TILE_SIZE
			walls.add(tile)
		elif data[i][1] == 'F':
			tile = FloorTile()
			tile.rect.x = col * TILE_SIZE
			tile.rect.y = row * TILE_SIZE
			floors.add(tile)

	robbermap[ry][rx] = '_'

	return rx, ry, robbermap, tilemap, cameras, robots, walls, floors
