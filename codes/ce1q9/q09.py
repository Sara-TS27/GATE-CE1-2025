import numpy as np

# Number of bulbs
N = 7

# Adjacency matrix A where A[i, j] = 1 if |i - j| == 1 else 0
A = np.zeros((N, N), dtype=int)
for i in range(N):
    for j in range(N):
        if abs(i - j) == 1:
            A[i, j] = 1

# Initial state: vector x_0 with only the 4th bulb ON (1-indexed)
x = np.array([0, 0, 0, 1, 0, 0, 0])

# Perform 8 update steps
for k in range(1, 9):
    # s_k = A @ x_k gives the number of ON neighbors for each bulb
    s = A @ x
    
    # Update rule: x_{k+1} = x_k + (1 - x_k)*(s == 1) - x_k*(s == 2)
    x = x + (1 - x) * (s == 1) - x * (s == 2)

# Output the result
on_bulbs = np.sum(x)
print(f"State after Step 8: {x}")
print(f"Number of ON bulbs: {on_bulbs}")
