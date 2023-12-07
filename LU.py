import numpy as np
def decomposition_LU(A,threshold=1e-7):
    """
        Decomposes a square matrix A into its upper triangular matrix U and lower triangular matrix L.

        Args:
            A: A square NumPy array.

        Returns:
            L: The lower triangular matrix of the decomposition.
            U: The upper triangular matrix of the decomposition.
        """
    matrix = np.array(A,dtype='f')
    if len(matrix) != len(matrix[0]):
        return 'Please enter square function'
    if np.linalg.det(matrix) == 0:
        return 'Infinitely many or no solutions'
    else:
        n = len(matrix)
        L = np.eye(n)
        U = matrix.copy()
        for k in range(n):
            for i in range(k+1,n):
                L[i][k] = U[i][k] / U[k][k]
                for j in range(k,n):
                    U[i][j] = U[i][j] - (L[i][k] * U[k][j])
        U[np.abs(U) < threshold] = 0
    return L , U

def system_resolution(L,U,b):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)
    # Etape de substitution avant (Ly = b)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] = y[i] - (L[i][j] * y[j])
    # Etape de substitution arrière (Ux = y)
    for i in range(n-1,-1,-1):
        x[i] = y[i]
        for j in range(i+1,n):
            x[i] = x[i] - (U[i][j] * x[j])
        x[i] = x[i] / U[i][i]
    return x

def fill_matrix(n,m):
    matrix = []
    for l in range(n):
        vector = []
        for c in range(m):
            element = float(input(f'Enter The Element number {l+1}{c+1}: '))
            vector.append(element)
        matrix.append(vector)
    return matrix
def fill_vector(n):
    vector = []
    for i in range(n):
        element = float(input(f'\nEnter The Element number {i+1}: '))
        vector.append(element)
    return vector

n = int(input('\nEnter The number of lignes: '))
m = int(input('\nEnter The number of Colomnes: '))
print('\nFill The Matrix A: \n')
a = fill_matrix(n,m)
print('\nFill The Vector B: \n')
b = fill_vector(n)
# a1 = [[3,-7,-2,2],
#      [-3,5,1,0],
#      [6,-4,0,-5],
#      [-9,5,-5,12]]
# b1 = [-9,5,7,11]

L , U = decomposition_LU(a)
print(f'\nL = \n {L}\n\n')
print(f'\nU = \n {U}\n\n')
print(f'\nx = {system_resolution(L, U, b)}\n')


