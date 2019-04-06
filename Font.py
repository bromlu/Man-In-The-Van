#!/usr/bin/python3

import contextlib
with contextlib.redirect_stdout(None): import pygame

pygame.font.init()

# Supporting Functions
def wrap(n, mi, ma):
	r = ma - mi + 1
	if n > ma:
		n = mi + ((n - ma) % r) - 1
	elif n < mi:
		n = ma - ((mi - n) % r - 1)
	
	return n

def get_sign(n):
	if n >= 0:
		return 1
	return -1

def str_get(s, size, color):
	font = pygame.font.Font('assets/Righteous.ttf', size)
	return font.render(s, True, color)

def str_draw(screen, font_surf, x, y, code):
	font_rect = font_surf.get_rect()
	if code == 'cx':
		font_rect.center = (x, y)
	elif code == 'tc':
		font_rect.midtop = (x, y)
	elif code == 'tl':
		font_rect.topleft = (x, y)
	else:
		font_rect.topright = (x, y)
	screen.blit(font_surf, font_rect)

def cxgetRect(s, size, y):
	font_surf = str_get(s, size, pygame.Color(255, 255, 255, 255))
	font_rect = font_surf.get_rect()
	font_rect.center = (480, y)
	return font_rect

def cxprint(screen, surface, s, size, color, y):
	font_surf = str_get(s, size, color)
	str_draw(screen, font_surf, surface.get_width() / 2, y, 'cx')

def tcprint(screen, surface, s, size, color, y):
	font_surf = str_get(s, size, color)
	str_draw(screen, font_surf, surface.get_width() / 2, y, 'tc')

def tlprint(screen, s, size, color, x, y):
	font_surf = str_get(s, size, color)
	str_draw(screen, font_surf, x, y, 'tl')

def trprint(screen, s, size, color, x, y):
	font_surf = str_get(s, size, color)
	str_draw(screen, font_surf, x, y, 'tr')

