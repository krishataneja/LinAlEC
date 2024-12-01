def COB(B1, B2):
    def inverse_matrix(M):
        n = len(M)
        augmented = [row + [int(i == j) for j in range(n)] for i, row in enumerate(M)]
        for i in range(n):
            if augmented[i][i] == 0:
                for j in range(i + 1, n):
                    if augmented[j][i] != 0:
                        augmented[i], augmented[j] = augmented[j], augmented[i]
                        break
            for j in range(i + 1, n):
                factor = augmented[j][i] / augmented[i][i]
                augmented[j] = [augmented[j][k] - factor * augmented[i][k] for k in range(2 * n)]
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                factor = augmented[j][i] / augmented[i][i]
                augmented[j] = [augmented[j][k] - factor * augmented[i][k] for k in range(2 * n)]
        return [row[n:] for row in augmented]

    def matrix_multiply(A, B):
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                row.append(sum(A[i][k] * B[k][j] for k in range(len(B))))
            result.append(row)
        return result

    def extract_columns(M):
        return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]

    B1_inv = inverse_matrix(B1)
    change_of_basis = matrix_multiply(B2, B1_inv)
    return extract_columns(change_of_basis)

B1 = [[1, 0], [0, 1]]
B2 = [[2, 1], [1, 2]]
print("change of basis matrix:", COB(B1, B2))
