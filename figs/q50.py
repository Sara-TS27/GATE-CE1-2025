import numpy as np
import matplotlib.pyplot as plt

theta = np.radians(45)
L = 2.0

A = np.array([0, L * np.sin(theta)])
B = np.array([L * np.cos(theta), 0])

plt.figure(figsize=(5, 5))

plt.plot([0, 0], [0, L + 0.5], 'k-', linewidth=3)
plt.plot([0, L + 0.5], [0, 0], 'k-', linewidth=3)

plt.plot([A[0], B[0]], [A[1], B[1]], 'b-o', linewidth=3, label=r'Rod ($\theta=45^\circ$)')

plt.text(A[0] - 0.2, A[1], 'Block A', fontsize=11)
plt.text(B[0], B[1] - 0.2, 'Block B', fontsize=11)

arc_theta = np.linspace(0, theta, 30)
plt.plot(0.4 * np.cos(arc_theta), 0.4 * np.sin(arc_theta), 'r--')
plt.text(0.45, 0.15, r'$\theta=45^\circ$', color='red')

plt.xlim(-0.5, L + 0.5)
plt.ylim(-0.5, L + 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle=':', alpha=0.6)
plt.title('Blocks A and B Connected by a Rigid Rod')
plt.savefig('q50.pdf')
plt.close()
