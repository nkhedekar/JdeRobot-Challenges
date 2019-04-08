from cgol import CGOL
import numpy as np
import json
import unittest

class TestCgolMethods(unittest.TestCase):

	def setUp(self):
		self.g = CGOL()
		with open('config.json') as config_fd:
			config = json.load(config_fd)
		self.grid_width = np.clip(config['width'], 8, 30)
		self.grid_height = np.clip(config['height'], 8, 30)

	def test_created_grid(self):
		np.testing.assert_array_equal(self.g.get_grid(), np.zeros((self.grid_width, self.grid_height)))

	def test_pattern_placement(self):
		self.g.add_object(self.g.BEACON, 0, 0)
		self.g.add_object(self.g.BLOCK, 10, 10)
		test_grid = np.zeros((self.grid_width, self.grid_height))
		test_grid[0:4, 0:4] = np.array([[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]])
		test_grid[10:12, 10:12] = np.array([[1, 1], [1, 1]])
		np.testing.assert_array_equal(self.g.get_grid(), test_grid)

	def test_still_life(self):
		self.g.add_object(self.g.BLOCK, 0, 0)
		self.g.add_object(self.g.BEEHIVE, 6, 0)
		self.g.add_object(self.g.TUB, 6, 12)
		self.g.update_grid()
		test_grid = np.zeros((self.grid_width, self.grid_height))
		test_grid[0:2, 0:2] = np.array([[1, 1], [1, 1]])
		test_grid[6:9, 0:4] = np.array([[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]])
		test_grid[6:9,12:15] = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
		np.testing.assert_array_equal(self.g.get_grid(), test_grid)
	
	def test_oscillators(self):
		self.g.add_object(self.g.BLINKER, 0, 0)
		self.g.add_object(self.g.TOAD, 6, 0)
		self.g.add_object(self.g.BEACON, 6, 12)
		self.g.update_grid()
		test_grid = np.zeros((self.grid_width, self.grid_height))
		test_grid[0:3, 0:3] = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
		test_grid[6:10, 0:4] = np.array([[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]])
		test_grid[6:10,12:16] = np.array([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])
		np.testing.assert_array_equal(self.g.get_grid(), test_grid)
	
	def test_spaceships(self):
		self.g.add_object(self.g.GLIDER, 0, 0)
		self.g.add_object(self.g.LIGHTSPACESHIP, 12, 5)
		self.g.update_grid()
		test_grid = np.zeros((self.grid_width, self.grid_height))
		test_grid[0:3, 1:4] = np.array([[1, 0, 0], [0, 1, 1], [1, 1, 0]])
		test_grid[12:16, 5:10] = np.array([[0, 1, 1, 1, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 0, 0, 1, 0]])
		np.testing.assert_array_equal(self.g.get_grid(), test_grid)
	
if __name__ == '__main__':
	unittest.main()