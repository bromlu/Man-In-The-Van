import contextlib
with contextlib.redirect_stdout(None): import pygame

from Tiles import WallTile, FloorTile
from Camera import Camera
from Robot import Robot
from Lazer import Lazer
from Constants import TILE_SIZE

width = 24
height = 18

def makeCamera(data, i, col, row):
	walls = [
		int(data[i-width-1][1]) % 2 == 1,
		int(data[i-width][1]) % 2 == 1,
		int(data[i-width+1][1]) % 2 == 1,
		int(data[i-1][1]) % 2 == 1,
		False,
		int(data[i+1][1]) % 2 == 1,
		int(data[i+width-1][1]) % 2 == 1,
		int(data[i+width][1]) % 2 == 1,
		int(data[i+width+1][1]) % 2 == 1,
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
	lazers = pygame.sprite.Group()
	
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

		if(data[i][0] == 'L'):
			foundPair = False
			for x in range(i+width, len(data) - 1, width):
				print(data[x])
				if data[x] and data[x][0] == 'L':
					foundPair = True
					lazer = Lazer((col * TILE_SIZE, row * TILE_SIZE), TILE_SIZE/8, abs(row*TILE_SIZE - int(x/width) * TILE_SIZE) + TILE_SIZE)
					lazers.add(lazer)
					data[x][0] == '_'
					break
			if not foundPair:
				for x in range(i+1, (row+1) * width, 1):
					if data[x] and data[x][0] == 'L':
						lazer = Lazer((col * TILE_SIZE, row * TILE_SIZE), abs(col*TILE_SIZE - int(x % width) * TILE_SIZE) + TILE_SIZE, TILE_SIZE/8)
						lazers.add(lazer)
						data[x][0] == '_'
						break

		tileNum = int(data[i][1:])
		if tileNum % 2 == 1:
			tile = WallTile((col * TILE_SIZE, row * TILE_SIZE), tileNum)
			walls.add(tile)
		elif tileNum % 2 == 0:
			tile = FloorTile((col * TILE_SIZE, row * TILE_SIZE), tileNum)
			floors.add(tile)

	robbermap[ry][rx] = '_'

	return rx, ry, robbermap, tilemap, cameras, robots, walls, floors, lazers
