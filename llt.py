
import numpy as np


M = np.matrix('5 1 3; 1 2 0; 3 0 7')
print('M: ')
print(M)
print('DET: ')
print(np.linalg.det(M))
print('Cholesky: ')
print(np.linalg.cholesky(M))

U = np.linalg.cholesky(M)
W = np.transpose(U) * U

print('W: ')
print(W)
