import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0, 2 * np.pi, 0.01)
x = np.exp(1j * t)
B = np.array([[1, 3],
              [2, 4]])

plt.plot(x.real, x.imag)


X1 = [point.real for point in x]
Y1 = [point.imag for point in x]
cx = np.vstack((X1, Y1))

z = np.dot(B, cx)

plt.plot(z[0, :], z[1, :], label='B * cx')
plt.xlabel('Real')
plt.ylabel('Imaginary')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.legend()
plt.show()
