#!/usr/bin/env python3
import json
import time
import numpy as np

class CGOL:
	ON = 1
	OFF = 0
	vals = [ON, OFF]

	# Still Lifes
	BLOCK = np.array([[1,1],[1,1]])
	BEEHIVE = np.array([[0,1,1,0],[1,0,0,1],[0,1,1,0]])
	TUB = np.array([[0,1,0],[1,0,1],[0,1,0]])

	# Oscillators
	BLINKER = np.array([[0,0,0],[1,1,1],[0,0,0]])
	TOAD = np.array([[0,0,0,0],[0,1,1,1],[1,1,1,0],[0,0,0,0]])
	BEACON = np.array([[1,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,1]])

	# Spaceships
	GLIDER = np.array([[0,0,1],[1,0,1],[0,1,1]])
	LIGHTSPACESHIP = np.array([[0,0,1,1,0],[1,1,0,1,1],[1,1,1,1,0],[0,1,1,0,0]])

	def __init__(self):
		with open('config.json') as config_fd:
			config = json.load(config_fd)
		self.width = np.clip(config['width'], 8, 30)
		self.height = np.clip(config['height'], 8, 30)
		self.grid = np.zeros((self.width, self.height))
		self.wrap_around = config['wrap_around']
		self.generation = 1
		np.random.seed = config['random_seed']
		
	def random_grid(self):
		self.grid = np.random.choice(self.vals, size=(
			self.width, self.height), p=[1./3, 2./3])
	
	def add_object(self, ob, i, j):
		w, h = ob.shape
		i = np.clip(i, 0, self.width - w - 1)
		j = np.clip(j, 0, self.height - h - 1)
		self.grid[i:i+w, j:j+h] = ob

	def sum_of_neighbors(self, i, j):
		if self.wrap_around:
			return int(self.grid[(i-1) % self.width][(j-1) % self.height] +
                            self.grid[(i-1) % self.width][(j) % self.height] +
                            self.grid[(i-1) % self.width][(j+1) % self.height] +
                            self.grid[(i) % self.width][(j-1) % self.height] +
                            self.grid[(i) % self.width][(j+1) % self.height] +
                            self.grid[(i+1) % self.width][(j-1) % self.height] +
                            self.grid[(i+1) % self.width][(j) % self.height] +
                            self.grid[(i+1) % self.width][(j+1) % self.height])
		else:
			pass

	def update_grid(self):
		new_grid = self.grid.copy()
		for i in range(self.grid.shape[0]):
			for j in range(self.grid.shape[1]):
				n = self.sum_of_neighbors(i, j)
				if self.grid[i][j] == self.ON:
					if n < 2 or n > 3:
						new_grid[i][j] = self.OFF
				else:
					if n == 3:
						new_grid[i][j] = self.ON
		self.grid = new_grid
		self.generation += 1
	
	def get_grid(self):
		return self.grid

	def val_to_char(self, val):
		return "*" if val == self.ON else " "

	def move_cursor_up(self):
		print("\033[%dA" % (self.height+4))

	def move_cursor_down(self):
		print("\033[%dB" % (self.height+4))

	def display_grid(self):
		for row in self.grid:
			print(" ".join(map(self.val_to_char, row)))

	def run_once(self):
		print("Number of Live Cells: ", int(np.sum(self.grid)))
		print("Number of Dead Cells: ", int(
			self.width*self.height - np.sum(self.grid)))
		print("Generation: ", self.generation)
		self.display_grid()
		self.move_cursor_up()
		self.update_grid()