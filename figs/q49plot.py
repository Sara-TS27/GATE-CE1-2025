import numpy as np
import matplotlib.pyplot as plt

x_pts = np.array([-2, 1, 2])
y_pts = np.array([28, 4, 16])

P2 = lambda x: 5*x**2 - 3*x + 2

x_dense = np.linspace(-2.5, 2.5, 200)

plt.figure(figsize=(6, 4.5))
plt.plot(x_dense, P2(x_dense), 'b-', label=r'$P_2(x) = 5x^2 - 3x + 2$')
plt.scatter(x_pts, y_pts, color='red', zorder=5, label='Data Points')
plt.scatter([0], [P2(0)], color='green', zorder=5, label=r'$P_2(0) = 2$')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Second-Degree Interpolating Polynomial')
plt.legend()
plt.savefig('q49.pdf')
plt.close()
