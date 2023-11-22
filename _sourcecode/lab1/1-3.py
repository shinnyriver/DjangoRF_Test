import numpy as np

A = np.array([[2, -3, 1],
              [4, -1, 2],
              [5, -2, 3]])

B = np.array([1, 3, -2])

try:
    solution = np.linalg.solve(A, B)
    print("Solution:")
    print("x =", solution[0])
    print("y =", solution[1])
    print("z =", solution[2])

except np.linalg.LinAlgError:
    print("No solution found.")
