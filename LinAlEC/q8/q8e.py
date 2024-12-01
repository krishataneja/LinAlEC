def pseudo_inverse(A):
    try:
        def transpose(m):
            return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

        def matrix_multiply(mat1, mat2):
            rows_mat1 = len(mat1)
            cols_mat1 = len(mat1[0])
            cols_mat2 = len(mat2[0])
            res = [[0] * cols_mat2 for _ in range(rows_mat1)]
            for i in range(rows_mat1):
                for j in range(cols_mat2):
                    res[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(cols_mat1))
            return res

        def identity_matrix(size):
            return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

        def matrix_inversion(m):
            size = len(m)
            augmented = [row + identity_matrix(size)[i] for i, row in enumerate(m)]
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
            inv = [row[size:] for row in augmented]
            return inv

        transpose_matrix = transpose(A)
        multiply_result = matrix_multiply(transpose_matrix, A)
        inverse_result = matrix_inversion(multiply_result)
        return matrix_multiply(inverse_result, transpose_matrix)
    
    except Exception as r:
        return f"error occrred: {str(r)}"

A= [[1, 2], [3, 4], [5, 6]]
print(pseudo_inverse(A))
