import numpy as np
from matplotlib import pyplot as plt

# Given data
X = np.array([[0.69, 0.49],
              [-1.31, -1.21],
              [0.39, 0.99],
              [0.09, 0.29],
              [1.29, 1.09],
              [0.49, 0.79],
              [0.19, -0.31],
              [-0.81, -0.81],
              [-0.31, -0.31],
              [-0.71, -1.01]])

# Calculate the mean-centered data matrix
X_mean_centered = X - np.mean(X, axis=0)

# Calculate the correlation matrix
C = np.dot(X_mean_centered.T, X_mean_centered) / (X.shape[0] - 1)

# Find the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(C)

# Sort eigenvalues and corresponding eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Print the results
lambda1 = eigenvalues[0]
lambda2 = eigenvalues[1]
e1 = eigenvectors[:, 0]
e2 = eigenvectors[:, 1]

print("Eigenvalues:")
print("λ1 =", lambda1)
print("λ2 =", lambda2)
print("\nEigenvectors:")
print("e1 =", e1)
print("e2 =", e2)

# Feature vector
V = np.column_stack((e1, e2))

# Transform original dataset
Z = np.dot(X_mean_centered, V)

# Print the result
print("Transformed Dataset (Z):")
print(Z)

# Reconstruct the original dataset
X_reconstructed = np.dot(Z, V.T) + np.mean(X, axis=0)

# Print the result
print("Reconstructed Original Dataset (X_reconstructed):")
print(X_reconstructed)


# Plotting the original dataset X
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c='blue', marker='o', label='Original Dataset')
plt.title('Original Dataset (X)')
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend()

# Plotting the principal component dataset Z
plt.subplot(1, 2, 2)
plt.scatter(Z[:, 0], Z[:, 1], c='red', marker='o', label='Principal Component Dataset')
plt.title('Principal Component Dataset (Z)')
plt.xlabel('Z1')
plt.ylabel('Z2')
plt.legend()

plt.tight_layout()
plt.show()

