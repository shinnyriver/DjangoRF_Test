import numpy as np
from matplotlib import pyplot as plt

X = np.array([2, 1])
plt.scatter(X[0], X[1], color='red', label='Point X (2, 1)')

theta = np.radians(45)
A = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

Y = np.dot(A, X)
plt.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Y = AX')

plt.axis([-10, 10, -10, 10])

plt.xlabel('X')
plt.ylabel('Y')

plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

plt.legend()
plt.show()
