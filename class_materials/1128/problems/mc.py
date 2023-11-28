#### Problem: Estimating the Value of Pi using Monte Carlo Integration

#**Objective:**  
# Write a Python program to estimate the value of Pi using Monte Carlo
# integration. The program should generate random points within a square 
# and count how many fall inside a quarter circle. Identify and correct
# any errors in the implementation.

import random

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_samples)

# Number of samples
num_samples = 1000000
print(f"Estimated value of Pi: {estimate_pi(num_samples)}")

