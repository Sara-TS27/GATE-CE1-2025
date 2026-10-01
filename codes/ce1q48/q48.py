import numpy as np

# Function f(x) and its derivative f'(x)
def f(x):
    return np.exp(-x) - x

def df(x):
    return -np.exp(-x) - 1

# First approximation
x0 = 0.5

# Newton-Raphson iteration formula: x1 = x0 - f(x0) / f'(x0)
x1 = x0 - f(x0) / df(x0)

print(f"Second approximation x1 = {x1:.2f}")
