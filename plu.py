
import numpy as np
from scipy.linalg import lu

C = np.matrix('1 2 -1; 2 4 0; 0 1 -1')

print('C: ')
print(C)

P, L, U = lu(C)

print('P: ')
print(P)
print('L: ')
print(L)
print('U: ')
print(U)

print('---------------------------------------------------')

B = np.matrix('1 1 0 3; 2 1 -1 1; 3 -1 -1 2; -1 2 3 -1')
print('B: ')
print(B)
P, L, U = lu(B)

print('P: ')
print(P)
print('L: ')
print(L)
print('U: ')
print(U)


print('P*U*L: ')
print(P*U*L)
