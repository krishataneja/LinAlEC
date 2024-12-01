class LinearSystem:
    def __init__(self, A, b):
        self.A = A
        self.b = b
        if len(A) != len(b):
            raise ValueError("Error: Number of rows in A must match the size of b.")
        for row in A:
            if len(row) != len(A[0]):
                raise ValueError("Error: All rows in A must have the same number of columns.")

    def solve_plu(self):
        P, L, U = self.plu_decomposition(self.A)
        if P is None or L is None or U is None:
            return "Error: PLU decomposition failed."

        b_perm = self.permute(self.b, P)
        y = self.forward_substitution(L, b_perm)
        x = self.backward_substitution(U, y)

        return x

    def plu_decomposition(self, matrix):
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

    def permute(self, vec, P):
        return [sum(P[i][j] * vec[j] for j in range(len(vec))) for i in range(len(P))]

    def forward_substitution(self, L, b):
        n = len(L)
        y = [0] * n
        for i in range(n):
            y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
        return y

    def backward_substitution(self, U, y):
        n = len(U)
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
        return x

# Example usage
A_example = [
    [2, 1, 1],
    [1, 3, 2],
    [1, 2, 3]
]
b_example = [7, 10, 13]

try:
    system = LinearSystem(A_example, b_example)
    solution = system.solve_plu()
    print("Solution to the system:", solution)
except ValueError as e:
    print(e)
