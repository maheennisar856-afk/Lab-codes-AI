import numpy as np

# Define two 2x2 matrices
M1 = np.array([[1, 2],
               [0, 1]])
M2 = np.array([[1, 0],
               [5, 5]])

print("Matrix M1:")
print(M1)
print("Matrix M2:")
print(M2)

# Multiply matrices
result = np.dot(M1, M2)
print("Resultant matrix after multiplication:")
print(result)

# Transpose of the resultant matrix
transpose_result = np.transpose(result)
print("Transpose of resultant matrix:")
print(transpose_result)
