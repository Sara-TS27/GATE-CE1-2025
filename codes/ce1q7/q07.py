import numpy as np

# Given angles in degrees
alpha = np.radians(130.0)
beta = np.radians(50.0)

# Direction vectors for PR and QS from matrix formulations
m_PR = np.array([np.cos(alpha/2), np.sin(alpha/2)])
m_QS = np.array([-np.sin(beta/2), np.cos(beta/2)])

# Angle RTS between directions using dot product: cos(theta) = m_PR^T * m_QS
cos_rts = np.dot(m_PR, m_QS)
rts_deg = np.degrees(np.arccos(cos_rts))

print(f"Angle RTS: {rts_deg:.2f} degrees")
