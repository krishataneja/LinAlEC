def least_square_solution(A, b):
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
        
        # Ensure b is in correct matrix form (a column vector)
        if isinstance(b[0], list):
            b = b[0]
        
        A_transpose = transpose(A)
        A_transpose_A = matrix_multiply(A_transpose, A)
        A_transpose_A_inv = matrix_inversion(A_transpose_A)
        A_transpose_b = [[x] for x in b]  # Convert b to column matrix
        least_square_x = matrix_multiply(A_transpose_A_inv, A_transpose_b)
        
        return least_square_x
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

matrix_A = [[1, 2], [3, 4], [5, 6]]
vector_b = [7, 8, 9]
print(least_square_solution(matrix_A, vector_b))
