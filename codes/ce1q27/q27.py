import numpy as np

A = np.array([[9.0, 15.0],
              [15.0, 50.0]])

# Cholesky decomposition: A = L * L^T
L = np.linalg.cholesky(A)

l22 = L[1, 1]
print("Lower Triangular Matrix L:")
print(L)
print(f"Value of |l22| = {abs(l22)}")
