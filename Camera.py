import contextlib
with contextlib.redirect_stdout(None): import pygame

class Camera(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([10, 10])
       self.image.fill(pygame.Color(0,240,240,0))
       self.original_image = self.image
       self.angle = 0

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def update(self, keys_pressed):
        if pygame.K_LEFT in keys_pressed:
            self.angle += 1
            self.image = self.rot_center(self.original_image, self.angle)
        if pygame.K_RIGHT in keys_pressed:
            self.angle -= 1
            self.image = self.rot_center(self.original_image, self.angle)

    def rot_center(self, image, angle):
        loc = image.get_rect().center
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite

