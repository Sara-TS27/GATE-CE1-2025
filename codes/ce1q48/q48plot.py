import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.exp(-x) - x
df = lambda x: -np.exp(-x) - 1

x = np.linspace(0, 1, 200)
x0 = 0.5
x1 = x0 - f(x0)/df(x0)

plt.figure(figsize=(6, 4.5))
plt.plot(x, f(x), 'b-', label=r'$f(x) = e^{-x} - x$')
plt.axhline(0, color='black', linewidth=0.8)

# Tangent line at x0
tangent = f(x0) + df(x0) * (x - x0)
plt.plot(x, tangent, 'r--', label='Tangent at $x_0=0.5$')

plt.scatter([x0, x1], [f(x0), 0], color='black')
plt.text(x0, f(x0)+0.05, r'$x_0 = 0.5$', horizontalalignment='center')
plt.text(x1, -0.08, r'$x_1 \approx 0.57$', horizontalalignment='center')

plt.grid(True, linestyle=':', alpha=0.6)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton-Raphson Step for $f(x) = e^{-x} - x$')
plt.legend()
plt.savefig('q48.pdf')
plt.close()
