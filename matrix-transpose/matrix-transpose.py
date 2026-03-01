import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m, n = len(A), len(A[0])
    matrix =[[0 for i in range(m)] for i in range(n)]
    for i in range(m):
        for j in range(n):
            matrix[j][i] = A[i][j]

    return np.array(matrix)
