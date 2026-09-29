import numpy as np
import matplotlib.pyplot as plt

A_area = 500.0
E = 60e3
alpha = 12e-6
L = 3000.0
k_rod = (A_area * E) / L
k_spring = 2500.0

dT = np.linspace(0, 120, 100)
F_th = A_area * E * alpha * dT
F_spring = k_spring * (F_th / (k_rod + k_spring)) / 1000.0

plt.figure(figsize=(6, 4))
plt.plot(dT, F_spring, 'b-', linewidth=2)
plt.scatter([100], [7.2], color='red', zorder=5, label='At $\Delta T = 100^\circ$C: $F_{BC} = 7.2$ kN')

plt.grid(True, linestyle=':', alpha=0.6)
plt.xlabel(r'Temperature Rise $\Delta T$ ($^\circ$C)')
plt.ylabel('Spring Force $F_{BC}$ (kN)')
plt.title('Spring Force vs. Temperature Rise of Rod AB')
plt.legend()
plt.savefig('q51.pdf')
plt.close()
