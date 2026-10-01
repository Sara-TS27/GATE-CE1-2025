import numpy as np

# Direction vectors for members PQ and QR
m_PQ = np.array([1, 1]) / np.sqrt(2)
m_QR = np.array([1, -1]) / np.sqrt(2)

# Stiffness contribution from member PQ
# k_PQ = AE/L * (m_PQ @ m_PQ.T)
k_PQ = np.outer(m_PQ, m_PQ)

# Stiffness contribution from member QR
# k_QR = AE/L * (m_QR @ m_QR.T)
k_QR = np.outer(m_QR, m_QR)

# Total global stiffness matrix at Q (in units of AE/L)
K = k_PQ + k_QR

print("Stiffness matrix K (times L/AE):")
print(K)
