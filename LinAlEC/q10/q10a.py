def polardecomp(matrix):
    try:
        def transpose(mat):
            return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

        def matrix_multiply(mat1, mat2):
            rows_mat1 = len(mat1)
            cols_mat1 = len(mat1[0])
            cols_mat2 = len(mat2[0])
            result = [[0] * cols_mat2 for _ in range(rows_mat1)]
            for i in range(rows_mat1):
                for j in range(cols_mat2):
                    result[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(cols_mat1))
            return result

        def identity_matrix(size):
            return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

        def matrix_inversion(mat):
            size = len(mat)
            augmented = [row + identity_matrix(size)[i] for i, row in enumerate(mat)]
            for i in range(size):
                if augmented[i][i] == 0:
                    for j in range(i + 1, size):
                        if augmented[j][i] != 0:
                            augmented[i], augmented[j] = augmented[j], augmented[i]
                            break
                pivot = augmented[i][i]
                for k in range(2 * size):
                    augmented[i][k] /= pivot
                for j in range(size):
                    if j != i:
                        factor = augmented[j][i]
                        for k in range(2 * size):
                            augmented[j][k] -= factor * augmented[i][k]
            inverse = [row[size:] for row in augmented]
            return inverse

        def square_root(mat):
            size = len(mat)
            epsilon = 1e-9
            approx = identity_matrix(size)
            diff = epsilon + 1
            while diff > epsilon:
                prev = approx
                mid = matrix_multiply(approx, approx)
                approx = [[0.5 * (mid[i][j] + mat[i][j]) for j in range(size)] for i in range(size)]
                diff = sum(abs(prev[i][j] - approx[i][j]) for i in range(size) for j in range(size))
            return approx

        matrix_transpose = transpose(matrix)
        symmetric_part = matrix_multiply(matrix_transpose, matrix)
        U_part = square_root(symmetric_part)
        U_inverse = matrix_inversion(U_part)
        R_part = matrix_multiply(matrix, U_inverse)

        return U_part, R_part

    except Exception as e:
        return f"An error occurred: {str(e)}"

mat1= [[2, 1], [1, 3]]
U, R = polardecomp(mat1)
print("U:", U)
print("R:", R)
