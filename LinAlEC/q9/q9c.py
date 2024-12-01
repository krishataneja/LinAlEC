def is_similar(A, B):
    size = len(A)
    if size != len(B) or any(len(row) != size for row in A + B):
        return False

    def determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        det = 0
        for col in range(len(matrix)):
            minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * determinant(minor)
        return det

    return determinant(A) == determinant(B)


def COB_similar(A, B):
    if not is_similar(A, B):
        return None
    size = len(A)

    identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    # Constructing Change of Basis (an approximation for simplicity)
    P = [[(A[i][j] - B[i][j]) / 2 if i != j else 1 for j in range(size)] for i in range(size)]
    return P


A = [[2, 1], [1, 2]]
B = [[2, -1], [-1, 2]]

if is_similar(A, B):
    print("Matrices are similar.")
    print("Change of Basis Matrix:", COB_similar(A, B))
else:
    print("Matrices are not similar.")
