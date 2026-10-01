import numpy as np

# Given parameters
L = 3000.0         # mm (3 m)
A = 500.0          # mm^2
E = 60e3           # MPa (N/mm^2)
alpha = 12e-6      # per °C
delta_T = 100.0    # °C
k_spring = 2500.0  # N/mm

# Stiffness of rod AB
k_r = (A * E) / L   # N/mm

# Thermal force generated
F_th = A * E * alpha * delta_T  # N

# Reduced global system equation for unconstrained node B:
# (k_r + k_spring) * u_B = F_th
u_B = F_th / (k_r + k_spring)

# Force developed in the spring BC
F_BC = k_spring * u_B          # in Newtons
F_BC_kN = F_BC / 1000.0        # in kN

print(f"Displacement at joint B (u_B) = {u_B:.2f} mm")
print(f"Force in spring BC = {F_BC_kN:.1f} kN")
