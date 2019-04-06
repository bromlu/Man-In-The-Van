import contextlib
with contextlib.redirect_stdout(None): import pygame

from Tiles import WallTile, FloorTile
from Camera import Camera
from Robot import Robot

width = 24
height = 24

def makeCamera(data, i, col, row):
	rotation = 0
	minRotation = -90
	maxRotation = 90
	if data[i-width][1] == 'W':
		rotation = 90
		minRotation += 90
		maxRotation += 90
	if data[i+1][1] == 'W':
		rotation = 180
		minRotation += 90
		maxRotation += 90
	if data[i+width][1] == 'W':
		rotation = 270
		minRotation += 90
		maxRotation += 90
	return Camera((col * 50, row * 50), rotation, minRotation, maxRotation)

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
