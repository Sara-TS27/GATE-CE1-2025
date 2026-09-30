import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define f(x) = x / 2
def f(x):
    return x / 2.0

# Function inside the integral: f(x) * (x - f(x))
def integrand(x):
    return f(x) * (x - f(x))

# Verify the integral value over [0, 2]
integral_value, _ = quad(integrand, 0, 2)
print(f"Calculated integral value: {integral_value:.6f}") # Should be 2/3 ≈ 0.666667
print(f"f(1) = {f(1)}")

# --- Plotting ---
x = np.linspace(0, 2, 200)
y_upper_bound = x**2 / 4.0
y_actual = integrand(x)

fig, ax = plt.subplots(figsize=(7, 5))

# Plot upper bound x^2 / 4 and actual integrand
ax.plot(x, y_upper_bound, 'r--', label=r'Upper bound $\frac{x^2}{4}$')
ax.plot(x, y_actual, 'b-', label=r'$f(x)[x - f(x)]$ for $f(x) = \frac{x}{2}$')
ax.plot(1, f(1), 'ro', label=f'f(1) = {f(1)}')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Integrand attains upper bound only when $f(x) = \frac{x}{2}$')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend()

# Save plot to file
plt.savefig('figs/q36.pdf', bbox_inches='tight')
plt.close(fig)
