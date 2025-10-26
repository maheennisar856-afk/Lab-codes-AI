import numpy as np

# Define a 4x4 matrix
matrix = np.array([
    [6, 1, 1, 3],
    [4, -2, 5, 1],
    [2, 8, 7, 6],
    [3, 1, 9, 7]
])

print("Original Matrix:")
print(matrix)

# Calculate inverse
inverse_matrix = np.linalg.inv(matrix)
print("Inverse of the matrix:")
print(inverse_matrix)
