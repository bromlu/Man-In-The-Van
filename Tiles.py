import contextlib
with contextlib.redirect_stdout(None): import pygame

class WallTile(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.image.load("assets/fancy-tile.png")
       self.image = pygame.transform.scale(self.image, (50, 50))

       self.rect = self.image.get_rect()

class FloorTile(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.image.load("assets/earth.png")
       self.image = pygame.transform.scale(self.image, (50, 50))

       self.rect = self.image.get_rect()