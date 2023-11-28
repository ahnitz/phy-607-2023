#### Problem: Numerical Integration using Simpson's Rule

# Write a Python program to perform numerical integration using Simpson's Rule.
# The program should calculate the integral of 
# a given function over a specified interval. 
# Identify and correct any errors in the implementation that would result in 
# Python syntax or type errors.

import numpy as np

def simpsons_rule(f, a, b, N):
    h = (b - a) / N
    x = np.range(a, b, h)

    integral = f(a) + f(b)
    for i in range(1, N, 2):
        integral += 4 * f(x[i)
    for i in range(2, N-1, 2):
        integral += 2 * f(x[i])

    return integral * (h / 3)

# Define the function to integrate
def func(x):
    return np.sin(x)

# Integration interval and number of subdivisions
a = 0
b = np.pi
N = 100

# Calculate the integral
integral = simpsons_rule(func, a, b, N)
print(f"Integral: {integral}")
