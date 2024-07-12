# Python-Based Linear Algebra Pset
# NOTE: No test file is written for this Pset but valid conditions are specified throughout the documentation of this file

# Utilize numpy to enable faster runtime through vectorized calculations

import numpy as np

# Problem 1: Add and Subtract 3D Vectors (same dimensions)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Sum
vector_sum = a + b
print(f"Sum of vectors a and b: {vector_sum}")

# Difference
vector_difference = a - b
print(f"The difference of vectors a and b: {vector_difference}")


# Problem 2: Add and Subtract 2D Matrices (same dimensions)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Sum

matrix_sum = A + B
print(f"Sum of matrices A and B: {matrix_sum}")

# Difference
matrix_difference = A - B
print(f"Difference of matrices A and B: {matrix_difference}")


# Problem 3: Compute the dot product of two vectors (same dimensions)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# np.dot does matrix multiplication and in this case treats vector A as a 1x3 matrix and vector B as a 3x1 matrix to return the dot product
dot_product = np.dot(a, b)
print(f"Dot product of vectors a and b: {dot_product}")


# Problem 4: Multiply Two Matrices (column dimension of matrix A and row dimension of matrix B must be equal)

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

matrix_product = np.dot(A, B)
print(f"The product of matrices A and B: {matrix_product}")


# Problem 5: Find the magnitude of a 3D vector

a = np.array([1, 1, 2])

vector_magnitude = np.linalg.norm(a)
print(f"The magnitude of vector a: {vector_magnitude}")

# Problem 6: Transpose a 2x2 Matrix

A = np.array([[1, 2], [3, 4]])

transpose_matrix = A.T
print(f"The transpose of matrix A: {transpose_matrix}")
