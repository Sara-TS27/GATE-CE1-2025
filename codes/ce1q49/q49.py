import numpy as np

# Vandermonde matrix from given x values: [-2, 1, 2]
V = np.array([
    [1, -2, 4],
    [1,  1, 1],
    [1,  2, 4]
])

# Given y values
y = np.array([28, 4, 16])

# Solve for polynomial coefficients [c0, c1, c2] where P(x) = c0 + c1*x + c2*x^2
c = np.linalg.solve(V, y)

# Value of P(0) is simply the constant term c0
P_0 = c[0]

print(f"Coefficients (c0, c1, c2): {c}")
print(f"P2(0) = {round(P_0)}")
