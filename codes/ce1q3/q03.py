import numpy as np

# Conic 1: y = x^2  => x^2 - y = 0
V1 = np.array([[1.0, 0.0], [0.0, 0.0]])
u1 = np.array([[0.0], [-0.5]])
f1 = 0.0

# Conic 2: y = -x^2 - 2x - 1 => x^2 + 2x + y + 1 = 0
V2 = np.array([[1.0, 0.0], [0.0, 0.0]])
u2 = np.array([[1.0], [0.5]])
f2 = 1.0

# Radical axis (common chord) line parameter: x + y = -0.5
# Point on line (h) and direction vector (m)
h = np.array([[0.0], [-0.5]])
m = np.array([[1.0], [-1.0]])

# Line-Conic intersection discriminant: Delta = [m^T (V1*h + u1)]^2 - g(h)*(m^T * V1 * m)
mVm = (m.T @ V1 @ m).item()
Vh_u = V1 @ h + u1
mVhu = (m.T @ Vh_u).item()
gh = (h.T @ V1 @ h + 2 * u1.T @ h + f1).item()

delta = mVhu**2 - gh * mVm

print(f"Discriminant (Delta): {delta}")
if delta > 0:
    print("Number of intersection points: 2")
elif delta == 0:
    print("Number of intersection points: 1")
else:
    print("Number of intersection points: 0")
