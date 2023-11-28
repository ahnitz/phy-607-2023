#### Problem: Calculating Gravitational Force

# Write a Python function to calculate the gravitational force between two masses.
# The function should take the masses of two # objects and the distance between
# their centers as arguments. 
# Use the gravitational constant \( G = 6.674 \times 10^{-11} \, #\text{Nm}^2/\text{kg}^2 \).
# Identify and correct any errors in the implementation.

def gravitational_force(m1, m2, r):
    G = 6.674e-11  # Gravitational constant
    force = G * m1 * m2 / r  # Incorrect implementation
    return force

# Masses in kg and distance in meters
mass1 = 5.972e24  # Earth's mass
mass2 = 7.35e22   # Moon's mass
distance = 3.84e8 # Distance between Earth and Moon

print(f"Gravitational force: {gravitational_force(mass1, mass2, distance)} N")

