import contextlib
with contextlib.redirect_stdout(None): import pygame
from pygame import Vector2

class Camera(pygame.sprite.Sprite):

    def __init__(self, pos, rotation, minRotation, maxRotation):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/camera.png")
        
        # A reference to the original image to preserve the quality.
        self.orig_image = self.image
        self.pos = Vector2(pos)  # The original center position/pivot point.
        self.offset = Vector2(16, 0)
        self.rect = self.image.get_rect(center=pos+self.offset)
        self.angle = rotation
        self.minRotation = minRotation
        self.maxRotation = maxRotation
        self.width = self.rect.width
        self.height = self.rect.height
        self.rotate()

    def rotate(self):
        # Rotate the image.
        self.image = pygame.transform.rotozoom(self.orig_image, -self.angle, 1)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(self.angle)
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.pos+offset_rotated)

    def update(self, keys_pressed, tilemap):
        if pygame.K_LEFT in keys_pressed:
            self.angle += 5
            if self.angle > self.maxRotation:
                self.angle = self.maxRotation
            self.rotate()
            # self.image = self.rot_center(self.original_image, self.angle)
        if pygame.K_RIGHT in keys_pressed:
            self.angle -= 5
            if self.angle < self.minRotation:
                self.angle = self.minRotation
            self.rotate()
            # self.image = self.rot_center(self.original_image, self.angle)

