import numpy as np

# Define coefficient matrix A
A = np.array([[1, 1, 1], [1, 0, 2]])

# Calculate matrix rank and degrees of freedom
rank = np.linalg.matrix_rank(A)
num_variables = A.shape[1]
free_variables = num_variables - rank

# For a 2x3 matrix with rank 2, the directional vector of the solution
# is given by the cross product of the two row vectors
direction_vector = np.cross(A[0], A[1])

print(f"Rank of A: {rank}")
print(f"Number of variables: {num_variables}")
print(f"Free variables (n - r): {free_variables}")
print(f"Direction vector: {direction_vector}")

# Geometric Interpretation
if free_variables == 1:
    print("The system of equations represents a LINE (Option b).")
elif free_variables == 2:
    print("The system of equations represents a PLANE (Option a).")
elif free_variables == 0:
    print("The system of equations represents a POINT (Option d).")
