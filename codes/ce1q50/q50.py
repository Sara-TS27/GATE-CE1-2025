import numpy as np

# For theta = 45 degrees:
# tan(theta) = (1 - mu^2) / (2 * mu) => mu^2 + 2*mu - 1 = 0

# Coefficients of quadratic equation: 1*mu^2 + 2*mu - 1 = 0
coeffs = [1, 2, -1]

# Find roots of the equation
roots = np.roots(coeffs)

# Select the positive root for the friction coefficient
mu = [r for r in roots if r > 0][0]

print(f"Coefficient of static friction (mu) = {mu:.2f}")
