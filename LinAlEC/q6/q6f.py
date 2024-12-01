def change_basis(v, B1, B2):
    def find_inverse(M):
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

    def multiply_matrix_vector(A, v):
        return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]

    def get_change_of_basis_matrix(B1, B2):
        B1_inv = find_inverse(B1)
        COB = [[sum(B2[i][k] * B1_inv[k][j] for k in range(len(B1))) for j in range(len(B1_inv[0]))] for i in range(len(B2))]
        return COB

    COB_matrix = get_change_of_basis_matrix(B1, B2)
    return multiply_matrix_vector(COB_matrix, v)

B1 = [[1, 0], [0, 1]]
B2 = [[2, 1], [1, 2]]
v_B1 = [3, 4]
coordinates_in_B2 = change_basis(v_B1, B1, B2)
print("coordinates of v:", coordinates_in_B2)

