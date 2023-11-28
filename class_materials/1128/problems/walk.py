#### Problem: Simulating a Random Walk in 2D

# Write a Python program to simulate a two-dimensional random walk 
# and calculate the average distance from the origin after a given number 
# of steps. The walk should start at the origin (0,0) and at each step
# move one unit up, down, left, or right with equal probability. 
# Identify and correct any errors in the implementation.

import random
import numpy as np

def random_walk_2D(num_steps):
    x, y = 0, 0

    for _ in range(num_steps):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        else:
            pass 

    distance = np.sqrt(x**2 + y**2)
    return distance

# Number of steps
num_steps = 1000
average_distance = random_walk_2D(num_steps)
print(f"Average distance from origin: {average_distance}")
