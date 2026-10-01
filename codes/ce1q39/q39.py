import numpy as np

# Coefficient matrix for reactions: [HA, VA, VB]^T
A = np.array([
    [1, 0, 0],
    [0, 1, 1],
    [0, 0, 4]
])

# Force / Moment sum vector
b = np.array([-50, 90, 330])

# Solve for reaction forces: HA, VA, VB
reactions = np.linalg.solve(A, b)
HA, VA, VB = reactions

# Calculate bending moments
M_C = abs(3 * HA)          # Bending moment at C
M_E = abs(2 * VB)          # Bending moment at mid-span E

max_BM = max(M_C, M_E)

print(f"HA = {HA} kN, VA = {VA} kN, VB = {VB} kN")
print(f"Maximum Bending Moment = {max_BM} kN-m")
