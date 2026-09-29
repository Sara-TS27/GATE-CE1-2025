import numpy as np
import matplotlib.pyplot as plt

# Initial state and transition rules
steps = 9
N = 7
states = np.zeros((steps, N), dtype=int)
states[0] = [0, 0, 0, 1, 0, 0, 0]

A = np.zeros((N, N), dtype=int)
for i in range(N):
    if i > 0: A[i, i - 1] = 1
    if i < N - 1: A[i, i + 1] = 1

for k in range(steps - 1):
    s = A @ states[k]
    prev = states[k]
    next_state = prev.copy()
    for j in range(N):
        if prev[j] == 0 and s[j] == 1:
            next_state[j] = 1
        elif prev[j] == 1 and s[j] == 2:
            next_state[j] = 0
    states[k + 1] = next_state

plt.figure(figsize=(8, 5))
plt.imshow(states, cmap='binary', aspect='auto')
plt.xticks(range(N), [f'Bulb {i+1}' for i in range(N)])
plt.yticks(range(steps), [f'Step {i}' if i > 0 else 'Initial' for i in range(steps)])
plt.title('Bulb States Across Steps (0: OFF, 1: ON)')
plt.colorbar(ticks=[0, 1], label='State (0 = OFF, 1 = ON)')
plt.tight_layout()
plt.savefig('q09.pdf')
plt.close()
