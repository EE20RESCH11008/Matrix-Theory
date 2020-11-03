# Singular-value decomposition
from numpy import array
from scipy.linalg import svd
# define a matrix
import numpy as np
A = np.array([[42.4, 78.2], [16, -12], [-12, 9]])
# SVD
U, s, VT = svd(A)
print(" U = ")
print(U)
print("\n S = ")
print(s)
print("\n V = ")
print(VT)

