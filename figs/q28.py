import numpy as np
import matplotlib.pyplot as plt

# Define the coefficient matrix A and constant vector b
# Line 1: x + y = 7
# Line 2: 3x + y = 13
A = np.array([[1, 1], 
              [3, 1]])
b = np.array([7, 13])

# Solve the system of linear equations Ax = b
solution = np.linalg.solve(A, b)
x_val, y_val = solution[0], solution[1]

# Calculate x^3 + y^3
result = x_val**3 + y_val**3


# --- Plotting to verify line intersection ---
# Generate x values for plotting
x = np.linspace(0, 6, 100)

# Line 1: y = 7 - x
y1 = 7 - x

# Line 2: y = 13 - 3x
y2 = 13 - 3*x

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the lines
ax.plot(x, y1, label=r'$x + y = 7$', color='blue')
ax.plot(x, y2, label=r'$3x + y = 13$', color='green')

# Mark the intersection point
ax.plot(x_val, y_val, 'ro', label=f'Intersection ({int(x_val)}, {int(y_val)})')

# Formatting the plot
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Verification of Line Intersection')
ax.legend()
ax.set_xlim(0, 6)
ax.set_ylim(0, 10)

# Save the figure to file instead of showing it
plt.savefig('q28_figure.png', bbox_inches='tight')
plt.close(fig)
