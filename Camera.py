import contextlib
import math
with contextlib.redirect_stdout(None): import pygame
from pygame import Vector2

class Camera(pygame.sprite.Sprite):

	def __init__(self, pos, rotation, minRotation, maxRotation, multiplier, offset):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("assets/camera.png")

		# A reference to the original image to preserve the quality.
		self.orig_image = self.image
		self.pos = Vector2(pos)  # The original center position/pivot point.
		self.offset = Vector2(16, 0)
		self.rect = self.image.get_rect(center=pos+self.offset)
		self.angle = rotation
		self.orig_angle = rotation
		self.fov = 30
		self.dist = 400
		self.minRotation = minRotation
		self.maxRotation = maxRotation
		self.multiplier = multiplier
		self.selectOffset = offset
		self.width = self.rect.width
		self.height = self.rect.height
		self.rotate()
		self.held = False
		self.audio = pygame.mixer.Sound("assets/audio/soundFX/Moving Cameracamera_rewind.wav")

	def rotate(self):
		self.image = pygame.transform.rotozoom(self.orig_image, -self.angle, 1)
		offset_rotated = self.offset.rotate(self.angle)
		self.rect = self.image.get_rect(center=self.pos+offset_rotated)

	def update(self, keys_pressed, tilemap):
		if pygame.K_LEFT in keys_pressed or pygame.K_RIGHT in keys_pressed:
			if not self.held:
				self.audio.play()
				self.held = True
		else:
			self.audio.stop()
			self.held = False

		if pygame.K_LEFT in keys_pressed:
			self.angle += 5 * self.multiplier
			if self.angle > self.maxRotation:
				self.angle = self.maxRotation
			if self.angle < self.minRotation:
				self.angle = self.minRotation
			self.rotate()
		if pygame.K_RIGHT in keys_pressed:
			self.angle -= 5 * self.multiplier
			if self.angle > self.maxRotation:
				self.angle = self.maxRotation
			if self.angle < self.minRotation:
				self.angle = self.minRotation
			self.rotate()

	def getLightCone(self, segments=6):
		fov, dist = self.fov, self.dist
		cx, cy = self.rect.center
		angs = [(self.angle + (s/(segments-1) - 0.5) * fov) * math.pi / 180 for s in range(segments)]
		result = [(cx, cy)] + [
			(cx + dist * math.cos(a), cy + dist * math.sin(a))
			for a in angs
		]
		return result

	def isSeen(self, pos):
		cx,cy = self.rect.center
		px,py = pos
		rx,ry = px-cx, py-cy
		d2 = rx*rx + ry*ry
		ang = (math.atan2(ry, rx) * 180 / math.pi) % 360
		rang = abs(ang - self.angle % 360)
		if rang > 180: rang = abs(360 - rang)
		in_fov = rang < self.fov / 2
		close = d2 < self.dist * self.dist
		return in_fov and close

	def reset(self):
		self.angle = self.orig_angle
		self.rotate()
