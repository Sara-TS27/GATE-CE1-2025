import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 200)

plt.figure(figsize=(6, 4))
plt.plot(x, x / 2, label=r'$f(x) = x/2$', color='blue', linewidth=2)
plt.plot(x, x**2 / 4, '--', label=r'Upper bound $\frac{x^2}{4}$', color='red')

plt.fill_between(x, 0, x**2 / 4, color='red', alpha=0.1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Upper Bound $x^2/4$ and Optimal $f(x) = x/2$')
plt.legend()
plt.savefig('q36.pdf')
plt.close()
