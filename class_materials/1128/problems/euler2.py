#### Problem: Calculating the Trajectory of a Projectile with Air Resistance

# **Objective:**  
# Write a Python program to simulate the trajectory of a projectile 
# factoring in air resistance. The program should use Euler's method to 
# update the position and velocity of the projectile. Identify and 
# correct any errors in the implementation.

import numpy as np
import matplotlib.pyplot as plt

def projectile_motion_with_air_resistance(dt, total_time, initial_velocity,
                                          launch_angle, mass, drag_coefficient):
    g = 9.81  # Acceleration due to gravity (m/s^2)
    angle_rad = np.radians(launch_angle)

    # Initial conditions
    vx = initial_velocity * np.cos(angle_rad)
    vy = initial_velocity * np.sin(angle_rad)
    x, y = 0, 0

    # Lists to store trajectory points
    x_vals, y_vals = [x], [y]

    for _ in np.arange(0, total_time, dt):
        # Update velocities
        v = np.sqrt(vx**2 + vy**2)  # Speed
        ax = -drag_coefficient * vx * vx / mass
        ay = -g + (drag_coefficient * vy * vy / mass) 

        vx += ax * dt
        vy += ay * dt

        # Update positions
        x += vx * dt
        y += vy * dt

        x_vals.append(x)
        y_vals.append(y)

        # Stop if projectile hits the ground
        if y < 0:
            break

    return x_vals, y_vals

# Simulation parameters
dt = 0.01  # Time step
total_time = 20  # Total time in seconds
initial_velocity = 50  # m/s
launch_angle = 45  # degrees
mass = 1  # kg
drag_coefficient = 0.1  # Drag coefficient

x_trajectory, y_trajectory = projectile_motion_with_air_resistance(
        dt, total_time, initial_velocity, launch_angle, mass, drag_coefficient)

# Plotting
plt.plot(x_trajectory, y_trajectory)
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Projectile Trajectory with Air Resistance')
plt.show()
