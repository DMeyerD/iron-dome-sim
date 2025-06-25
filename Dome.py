import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravity (m/s^2)

# Initial rocket parameters
# TODO - Randomise later =
x0, y0 = 100, 0       # Starting position
vx = 15               # Horizontal velocity (m/s)
vy = 80               # Vertical velocity (m/s)

# Solve for time of impact: y(t) = 0
# Quadratic equation: 0 = y0 + vy*t - 0.5*g*t^2
# Rearranged: 0.5*g*t^2 - vy*t - y0 = 0
a = -0.5 * g
b = vy
c = y0

discriminant = b**2 - 4*a*c
if discriminant >= 0:
    t_impact = (-b - np.sqrt(discriminant)) / (2*a)
    x_impact = x0 + vx * t_impact
else:
    t_impact = None
    x_impact = None

# Generate trajectory data
t_values = np.linspace(0, t_impact, num=100)
x_values = x0 + vx * t_values
y_values = y0 + vy * t_values - 0.5 * g * t_values**2

# Plot the trajectory
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Rocket Trajectory', color='red')
plt.axhline(0, color='black', linestyle='--')
if x_impact:
    plt.plot(x_impact, 0, 'ko', label=f'Impact Point: {x_impact:.1f} m')

print(f"y min: {min(y_values)}, y max: {max(y_values)}")
plt.title("Rocket Trajectory with Gravity")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Vertical Position (m)")
plt.grid(True)
plt.legend()
plt.ylim(bottom=0)
plt.show()
