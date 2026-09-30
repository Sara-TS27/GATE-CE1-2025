import numpy as np

# System of linear equations:
# 1*x + 1*y = 7
# 3*x + 1*y = 13
A = np.array([[1, 1],
              [3, 1]])

b = np.array([7, 13])

# Solve Ax = b for (x, y)
solution = np.linalg.solve(A, b)
x, y = int(round(solution[0])), int(round(solution[1]))

# Calculate x^3 + y^3
result = x**3 + y**3

print(f"Calculated x: {x}")
print(f"Calculated y: {y}")
print(f"x^3 + y^3 = {result}")
