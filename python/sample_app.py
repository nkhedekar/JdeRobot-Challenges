from cgol import CGOL
import numpy as np
import time

print("Welcome to Nikhil Khedekar's solution for the Python Challenge of JDERobot for GSoC-2019!")

t = int(input("Please enter the time step value in ms (int): "))
t = np.clip(t, 50, 1000)
max_iterations = int(input("Please enter the maximum number of iterations (int): "))
max_iterations = np.clip(max_iterations, 10, 1000)

g = CGOL()
d = {1: g.BLOCK, 2: g.BEEHIVE, 3: g.TUB, 4: g.BLINKER, 5: g.TOAD, 6: g.BEACON, 7: g.GLIDER, 8: g.LIGHTSPACESHIP}

for _ in range(20):
	print("Please enter the number (1-8) of the pattern you would like to add to the grid or enter 9 for random. To start the game with the selected settings enter 0")
	print("0 Start Game\n1 Block \n2 Beehive\n3 Tub\n4 Blinker\n5 Toad\n6 Beacon\n7 Glider\n8 Light Space Ship\n9 Random Grid")
	selection = int(input("Your Choice: "))
	if selection == 0:
		break
	elif selection == 9:
		g.random_grid()
	else:
		i,j = map(int,input("Please enter the location for the pattern as two space-seperated integers: ").split())
		g.add_object(d[selection], i,j)

print("Press Ctrl+C at any point to exit. The program shall automatically exit after the maximum iterations.")
for counter in range(max_iterations):
	g.run_once()
	time.sleep(t/1000)
g.move_cursor_down()
print("Thank you for playing!")