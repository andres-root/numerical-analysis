
import numpy as np
from scipy.linalg import lu

# Factorizacion LU

A = np.matrix('1 1 0 3; 2 1 -1 1; 3 -1 -1 2; -1 2 3 -1')
A[1, :] = A[1, :] - 2*A[0, :]
A[2, :] = A[2, :] - 3*A[0, :]
A[3, :] = A[3, :] + A[0, :]
A[2, :] = A[2, :] - 4*A[1, :]
A[3, :] = A[3, :] + 3*A[1, :]
U1 = A
print(U1)
L = np.matrix('1 0 0 0; 2 1 0 0; 3 4 1 0; -1 -3 0 1')
W = L * U1
print(W)


# Factorizacion PLU
P, L, U = lu(A)
print('P')
print(P)
print('L')
print(L)
print('U')
print(U)
