#**Objective:**  
#Write a Python program to simulate a damped harmonic oscillator using Euler's
# method. The program should calculate the position and velocity of the 
# oscillator over time. Identify and correct any errors in the implementation.

import numpy as np
import matplotlib.pyplot as plt

def damped_oscillator(dt, total_time, omega_0, gamma):
    time_steps = int(total_time / dt)
    position = np.zeros(time_steps)
    velocity = np.zeros(time_steps)

    # Initial conditions
    position[0] = 1.0  # Initial position
    velocity[0] = 0.0  # Initial velocity

    for i in range(1, time_steps):
        position[i] = position[i-1] + velocity[i-1] * dt
        velocity[i] = velocity[i-1] - omega_0 ** 2 * position[i-1] * dt - gamma * velocity[i] * dt

    return np.arange(0, total_time, dt), position, velocity

# Parameters
dt = 0.01  # Time step
total_time = 10  # Total time
omega_0 = 2*np.pi  # Natural frequency
gamma = 0.1  # Damping coefficient

time, position, velocity = damped_oscillator(dt, total_time, omega_0, gamma)

# Plotting
plt.plot(time, position, label='Position')
plt.plot(time, velocity, label='Velocity')
plt.xlabel('Time')
plt.ylabel('Position / Velocity')
plt.legend()
plt.show()

