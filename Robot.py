import contextlib
with contextlib.redirect_stdout(None): import pygame

class Robot(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("assets/white-rumba-nice.png")
		self.image = pygame.transform.scale(self.image, (50, 50))

		self.rect = self.image.get_rect()
		self.width = self.rect.width
		self.height = self.rect.height

	def update(self, keys_pressed, tilemap):
		pass
	# if pygame.K_LEFT in keys_pressed and self.checkBounds(tilemap, self.rect.x - 1, self.rect.y):
	#     self.rect.x -= 1
	# if pygame.K_RIGHT in keys_pressed and self.checkBounds(tilemap, self.rect.x + 1, self.rect.y):
	#     self.rect.x += 1
	# if pygame.K_UP in keys_pressed and self.checkBounds(tilemap, self.rect.x, self.rect.y - 1):
	#     self.rect.y -= 1
	# if pygame.K_DOWN in keys_pressed and self.checkBounds(tilemap, self.rect.x, self.rect.y + 1):
	#     self.rect.y += 1



