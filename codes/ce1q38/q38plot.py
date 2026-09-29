import numpy as np
import matplotlib.pyplot as plt

P = np.array([0, 0])
Q = np.array([1, 1])
R = np.array([2, 0])

plt.figure(figsize=(6, 4))
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'b-o', linewidth=2, label='Member PQ')
plt.plot([Q[0], R[0]], [Q[1], R[1]], 'r-o', linewidth=2, label='Member QR')

# Annotations & DOF arrows
plt.quiver(Q[0], Q[1], 0.3, 0, angles='xy', scale_units='xy', scale=1, color='green', label='u (Horizontal DOF)')
plt.quiver(Q[0], Q[1], 0, 0.3, angles='xy', scale_units='xy', scale=1, color='purple', label='v (Vertical DOF)')

plt.text(P[0]-0.1, P[1]-0.1, 'P (Hinge)', fontsize=11)
plt.text(Q[0], Q[1]+0.15, 'Q', fontsize=11)
plt.text(R[0]-0.1, R[1]-0.1, 'R (Hinge)', fontsize=11)

plt.xlim(-0.5, 2.5)
plt.ylim(-0.5, 1.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.title('Two-Member Truss with Degrees of Freedom (u, v) at Q')
plt.legend(loc='upper right')
plt.savefig('q38.pdf')
plt.close()
