import numpy as np
import matplotlib.pyplot as plt

# Define x grid
x = np.linspace(-3, 2, 400)

# Curves: y = x^2 and y = -x^2 - 2x - 1
y1 = x**2
y2 = -x**2 - 2*x - 1

# Pencil line: x + y = -0.5  =>  y = -x - 0.5
y_line = -x - 0.5

plt.figure(figsize=(10, 8))
plt.plot(x, y1, label=r'$y = x^2$', color='blue')
plt.plot(x, y2, label=r'$y = -x^2 - 2x - 1$', color='red')
plt.plot(x, y_line, '--', label=r'$x + y = -1/2$', color='green')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.title('Two Parabolas and Common Line')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('q03.pdf')
plt.close()
