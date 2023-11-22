import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [1, 1, 3]])

a2_3 = A[1, 2]
print("a) a23:", a2_3)

third_row = A[2, :]
print("b) 3rd row of A:",third_row)

second_col = A[:, 1]
print("c) 2nd column of A:", second_col)

A_transpose = A.T
print("d) Transpose of A:\n", A_transpose)

rank_A = np.linalg.matrix_rank(A)
print("e) Rank of A:", rank_A)

try:
    A_inverse = np.linalg.inv(A)
    print("f) Inverse of A:\n", A_inverse)
except np.linalg.LinAlgError:
    print("f) A is singular.")

diagonal_sum = np.trace(A)
print("g) Sum of diagonal elements of A:", diagonal_sum)

determinant_A = np.linalg.det(A)
print("h) Determinant of A:", determinant_A)

adjoint_A = np.linalg.inv(A) * determinant_A
print("i) Adjoint matrix of A:\n", adjoint_A)