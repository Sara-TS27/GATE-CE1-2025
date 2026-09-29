import numpy as np
import matplotlib.pyplot as plt

r = 1.0
alpha_deg, beta_deg = 130.0, 50.0
alpha, beta = np.radians(alpha_deg), np.radians(beta_deg)

# Points
P = np.array([-r, 0.0])
Q = np.array([r, 0.0])
O = np.array([0.0, 0.0])
R = np.array([r * np.cos(alpha), r * np.sin(alpha)])
S = np.array([r * np.cos(beta), r * np.sin(beta)])

# Intersection T of extended PR and QS
T = np.array([0.0, (r * np.sin(alpha)) / (1 + np.cos(alpha))])

# Circle points
theta = np.linspace(0, 2 * np.pi, 300)
x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x_circle, y_circle, 'b-', label='Circle')
plt.plot([P[0], T[0]], [P[1], T[1]], 'r--', label='Extended PR')
plt.plot([Q[0], T[0]], [Q[1], T[1]], 'g--', label='Extended QS')

# Draw segments
plt.plot([O[0], R[0]], [O[1], R[1]], 'k:')
plt.plot([O[0], S[0]], [O[1], S[1]], 'k:')

# Plot points
points = {'P': P, 'Q': Q, 'O': O, 'R': R, 'S': S, 'T': T}
for name, pt in points.items():
    plt.scatter(*pt, color='black')
    plt.text(pt[0] + 0.05, pt[1] + 0.05, name, fontsize=12)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.axis('equal')
plt.grid(True, linestyle=':', alpha=0.6)
plt.title('Circle Geometry with Intersection T')
plt.savefig('q07.pdf')
plt.close()
