import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')

# Plane 1: x + y + z = 0 => z = -x - y
# Plane 2: x + 2z = 0     => x = -2z
x_range = np.linspace(-3, 3, 20)
y_range = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x_range, y_range)

Z1 = -X - Y
Z2 = -0.5 * X

ax.plot_surface(X, Y, Z1, alpha=0.5, color='cyan', label='x + y + z = 0')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='orange', label='x + 2z = 0')

# Intersection Line: x = 2k, y = -k, z = -k
k = np.linspace(-1.5, 1.5, 100)
line_x = 2 * k
line_y = -k
line_z = -k

ax.plot(line_x, line_y, line_z, color='red', linewidth=3, label='Intersection Line')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Intersection of Two Planes')
plt.savefig('q12.pdf')
plt.close()
