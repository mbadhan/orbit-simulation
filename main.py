"""
Simple Newtonian planetary orbit simulation written in Python 3
Move the camera with WASD
"""

import pygame 
import sys
import time
from particle import *

width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
set_screen(screen)



world = World(100)
world.add(Particle((400, 100), 1, [100, 0]))
world.add(Particle((400, 300), 100000))
world.add(Particle((400, 600), 1, [-100, 0]))
world.add(Particle((400, 700), 1, [-100, 0]))
clock = pygame.time.Clock()


fps = 120
dt = 1/fps
camera_x = 0
camera_y = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				camera_x = -5
			elif event.key == pygame.K_d:
				camera_x = 5
			elif event.key == pygame.K_w:
				camera_y = -5
			elif event.key == pygame.K_s:
				camera_y = 5
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				camera_x = 0
			elif event.key == pygame.K_w or event.key == pygame.K_s:
				camera_y = 0


	screen.fill((0, 0, 0))


	world.update(1/fps)
	world.moveCam(camera_x, camera_y)
	world.draw()
	pygame.display.update()


	dt = clock.tick(fps)
