def LU(A):
    def decompose(matrix):
        n = len(matrix)
        L = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
        U = [[matrix[i][j] for j in range(n)] for i in range(n)]
        for col in range(n):
            if U[col][col] == 0:
                return None, None
            for row in range(col + 1, n):
                factor = U[row][col] / U[col][col]
                L[row][col] = factor
                for k in range(n):
                    U[row][k] -= factor * U[col][k]
        return L, U

    if len(A) != len(A[0]):
        return "Error: LU decomposition is only possible for square matrices."
    L, U = decompose(A)
    if L is None or U is None:
        return "Error: Matrix is singular, LU decomposition is not possible."
    return L, U

A_example = [
    [4, 3],
    [6, 3]
]

result = LU(A_example)
if isinstance(result, str):
    print(result)
else:
    L, U = result
    print("L (Lower Triangular Matrix):")
    for row in L:
        print(row)
    print("U (Upper Triangular Matrix):")
    for row in U:
        print(row)
