#code by Sara
import numpy as np

# Conic 1: x^2 - y = 0
V1 = np.array([[1.0, 0.0],
               [0.0, 0.0]])
u1 = np.array([0.0, -0.5])
f1 = 0.0

# Conic 2: x^2 + 2x + y + 1 = 0
V2 = np.array([[1.0, 0.0],
               [0.0, 0.0]])
u2 = np.array([1.0, 0.5])
f2 = 1.0

mu = -1.0  # eliminates the quadratic (x^2) part since V1 == V2
V = V1 + mu * V2
u = u1 + mu * u2
f = f1 + mu * f2

print("V1+mu*V2 =\n", V)          # -> zero matrix: confirms degeneracy
print("Line: 2*(%.3f)x + 2*(%.3f)y + %.3f = 0" % (u[0], u[1], f))

# Substitute the resultant line y = -x - 0.5 back into y = x^2
# x^2 + x + 0.5 = 0
coeffs = [1.0, 1.0, 0.5]
disc = coeffs[1] ** 2 - 4 * coeffs[0] * coeffs[2]
print("Discriminant of x^2 + x + 0.5 = 0:", disc)

roots = np.roots(coeffs)
print("Roots (complex if disc<0):", roots)

if disc < 0:
    print("No real intersection points -> answer: 0  [Option A]")
else:
    print("Number of real intersection points:", 1 if disc == 0 else 2)
