def PLU(A):
    def decompose(matrix):
        n = len(matrix)
        P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        L = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
        U = [row[:] for row in matrix]
        for col in range(n):
            max_row = col
            for row in range(col + 1, n):
                if abs(U[row][col]) > abs(U[max_row][col]):
                    max_row = row
            if U[max_row][col] == 0:
                return None, None, None
            if max_row != col:
                U[col], U[max_row] = U[max_row], U[col]
                P[col], P[max_row] = P[max_row], P[col]
            for row in range(col + 1, n):
                factor = U[row][col] / U[col][col]
                L[row][col] = factor
                for k in range(n):
                    U[row][k] -= factor * U[col][k]
        return P, L, U

    if len(A) != len(A[0]):
        return "Error: PLU decomposition is only possible for square matrices."
    P, L, U = decompose(A)
    if P is None or L is None or U is None:
        return "Error: Matrix is singular, PLU decomposition is not possible."
    return P, L, U

A_example = [
    [2, 1, 1],
    [4, 3, 3],
    [8, 7, 9]
]

result = PLU(A_example)
if isinstance(result, str):
    print(result)
else:
    P, L, U = result
    print("P (Permutation Matrix):")
    for row in P:
        print(row)
    print("L (Lower Triangular Matrix):")
    for row in L:
        print(row)
    print("U (Upper Triangular Matrix):")
    for row in U:
        print(row)
