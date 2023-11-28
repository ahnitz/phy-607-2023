#### Problem: Solving a System of Linear Equations using NumPy

# Write a Python program to solve a system of linear equations using NumPy.
#  The system can be represented as \(Ax = b\), where \(A\) is a matrix of 
# coefficients, \(x\) is the vector of unknowns, and \(b\) is the
# right-hand side vector. Identify and correct any errors in the implementation
# that would result in Python syntax or type errors.

import numpy as np

def solve_linear_system(A, b):
    A_matrix = np.array[A]  
    b_vector = np.array(b)

    x = np.linearsolve(A_matrix, b_vector)  
    return x

# Coefficients and right-hand side
A = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]
b = [1, -2, 0]

# Solve the system
solution = solve_linear_system(A, b)
print(f"Solution of the system: {solution}")
