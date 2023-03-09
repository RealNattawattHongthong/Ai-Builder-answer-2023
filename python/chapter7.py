'''
def MatrixDeterminant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for j in range(n):
            det += ((-1)**j)*matrix[0][j]*MatrixDeterminant([[matrix[i][k] for k in range(n) if k!=j] for i in range(1,n)])
        return det
matrix = [[1,2,3],[4,5,6],[7,8,9]]
det = MatrixDeterminant(matrix)
print(det) # 0
'''
import numpy as np

def MatrixDeterminant(str):
    rows = str.split("<>")
    n_rows = len(rows)
    
    # Check if it is a square matrix
    for i in range(n_rows):
        if len(rows[i].split()) != n_rows:
            return -1
    
    matrix = np.array([row.split() for row in rows], dtype=int)
    
    # Check if it is a square matrix
    if matrix.shape[0] != matrix.shape[1]:
        return -1
    
    return int(round(np.linalg.det(matrix)))
print(MatrixDeterminant("1 2 3 4 5 6 7 8 9")) 