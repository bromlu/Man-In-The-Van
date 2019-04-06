import contextlib
with contextlib.redirect_stdout(None): import pygame

from Tiles import WallTile, FloorTile
from Camera import Camera
from Robot import Robot

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
		offset = (50, 0)
		multiplier = -1
	elif(walls[7] and not walls[3] and not walls[5]):
		rotation = 270
		range = 180
		offset = (0, 50)
		multiplier = -1

	if(walls[0] and not walls[1] and not walls[3]):
		rotation = 45
		range = 270
	elif(walls[2] and not walls[1] and not walls[5]):
		rotation = 135
		range = 270
		offset = (50, 0)
	elif(walls[6] and not walls[3] and not walls[7]):
		rotation = 315
		range = 270
		offset = (0, 50)
		multiplier = -1
	elif(walls[8] and not walls[5] and not walls[7]):
		multiplier = -1
		rotation = 225
		range = 270
		offset = (50, 50)

	if(walls[0] and walls[1] and walls[3]):
		rotation = 45
		range = 90
	elif(walls[2] and walls[1] and walls[5]):
		rotation = 135
		range = 90
		offset = (50, 0)
	elif(walls[6] and walls[3] and walls[7]):
		rotation = 315
		range = 90
		offset = (0, 50)
		multiplier = -1
	elif(walls[8] and walls[5] and walls[7]):
		rotation = 225
		range = 90
		offset = (50, 50)
		multiplier = -1

	return Camera((col * 50 + offset[0], row * 50 + offset[1]), rotation, rotation - range/2, rotation + range/2, multiplier, offset)

def loadLevel(levelText):
	file = open(levelText, "r" )
	data = file.read().replace("\n", " ").split(" ")
	file.close()

	robbermap = []
	rx = 0
	ry = 0
	tilemap = []
	spritemap = pygame.sprite.Group()
	objectmap = pygame.sprite.Group()
	
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
			objectmap.add(makeCamera(data, i, col, row))
		if(data[i][0] == 'M'):
			robot = Robot()
			robot.rect.x = col * 50
			robot.rect.y = row * 50
			objectmap.add(robot)

		if data[i][1] == 'W':
			tile = WallTile()
		elif data[i][1] == 'F':
			tile = FloorTile()
		tile.rect.x = col * 50
		tile.rect.y = row * 50
		spritemap.add(tile)

	robbermap[ry][rx] = '_'

	return rx, ry, robbermap, tilemap, spritemap, objectmap
