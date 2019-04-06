import contextlib
with contextlib.redirect_stdout(None): import pygame

from Tiles import WallTile, FloorTile

def loadLevel(levelText):
    file = open(levelText, "r" )
    data = file.read().replace("\n", "").replace("  ", " ").split(" ")
    file.close()
    map = pygame.sprite.Group()
    tile = None
    for i in range(len(data)):
        print(data[i])
        if data[i] == "W" or data[i] == "CW":
            tile = WallTile()
        if data[i] == "F" or data[i] == "RF":
            tile = FloorTile()
        print(tile)
        tile.rect.x = (i % 24) * 10
        tile.rect.y = int(i / 24) * 10
        map.add(tile)

    return map