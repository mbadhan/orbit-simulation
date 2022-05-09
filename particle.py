import pygame 
import math
import numpy as np

screen = 0

def set_screen(x):
	global screen 
	screen = x

class Particle:
	def __init__(self, pos, mass, vel=np.array([0, 0], dtype='float')):
		self.pos = np.array(pos, dtype='float') 
		self.mass = mass 
		self.velocity = np.array(vel, dtype='float')
		self.force = np.array([0, 0], dtype='float')
		self.radius = 5
	
	def draw(self, camera):
		int_pos = int(self.pos[0] - camera[0]), int(self.pos[1] - camera[1])
		pygame.draw.circle(screen, (255, 255, 255), int_pos, int(self.radius))

	def update(self, dt):
		acceleration = self.force / self.mass
		self.velocity += acceleration * dt
		self.pos += self.velocity * dt



class World:

	def __init__(self, g = 500, stuff=[]):
		self.stuff = stuff 
		self.G = g
		self.camera = np.array([0, 0])
	
	def calculate_forces(self):
		force = np.array([0, 0], dtype='float')
		for i in range(len(self.stuff)):
			force = np.array([0, 0], dtype='float')
			for j in range(len(self.stuff)):
				if j != i:
					pos1 = self.stuff[i].pos
					pos2 = self.stuff[j].pos
					radius = np.linalg.norm(pos1-pos2)
					radius_sqred = radius**2 + 0.00001
					# f_g is a scalar
					f_g = self.G * self.stuff[i].mass * self.stuff[j].mass / radius_sqred
					# force_j is a vector
					force_j = f_g * (pos2-pos1)/radius 
					force += force_j

			self.stuff[i].force = force

	def update(self, dt):
		self.calculate_forces()
		for i in self.stuff:
			i.update(dt)

	def draw(self):
		for i in self.stuff:
			i.draw(self.camera)
	
	def add(self, x):
		self.stuff.append(x)
	
	def moveCam(self, x, y):
		self.camera[0] += x
		self.camera[1] += y