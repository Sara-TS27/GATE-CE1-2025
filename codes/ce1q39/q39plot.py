import matplotlib.pyplot as plt

# Frame Geometry: A(0,0), C(0,3), E(2,3), D(4,3), B(4,0)
frame_x = [0, 0, 2, 4, 4]
frame_y = [0, 3, 3, 3, 0]

plt.figure(figsize=(7, 5))
plt.plot(frame_x, frame_y, 'k-', linewidth=3, label='Plane Frame')

# Applied Loads
plt.quiver(0, 3, 0.8, 0, angles='xy', scale_units='xy', scale=1, color='red', label='50 kN Horizontal')
plt.quiver(2, 3, 0, -0.8, angles='xy', scale_units='xy', scale=1, color='blue', label='90 kN Vertical')

# Bending Moment Envelope Visualization
plt.plot([-0.5, 0], [3, 3], 'm--')
plt.plot([0, -0.5], [0, 3], 'm-', alpha=0.7, label='BM Diagram')

plt.plot([0, 2, 4], [3.5, 3.55, 3], 'm-')

plt.text(0, 0, ' A (Hinge)', verticalalignment='top')
plt.text(4, 0, ' B (Roller)', verticalalignment='top')
plt.text(0, 3, 'C', verticalalignment='bottom')
plt.text(2, 3, 'E', verticalalignment='bottom')
plt.text(4, 3, 'D', verticalalignment='bottom')

plt.xlim(-1.5, 5.5)
plt.ylim(-0.5, 4.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.title('Frame Loading and Bending Moment Diagram')
plt.legend()
plt.savefig('q39.pdf')
plt.close()
