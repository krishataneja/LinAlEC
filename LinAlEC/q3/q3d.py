def dim_and_basis(S):
    def row_echelon_form(matrix):
        rows, cols = len(matrix), len(matrix[0])
        pivot_row = 0
        for col in range(cols):
            if pivot_row >= rows:
                break
            if matrix[pivot_row][col] == 0:
                for r in range(pivot_row + 1, rows):
                    if matrix[r][col] != 0:
                        matrix = swap_rows(matrix, pivot_row, r)
                        break
            if matrix[pivot_row][col] != 0:
                scale = 1 / matrix[pivot_row][col]
                matrix = scale_row(matrix, pivot_row, scale)
                for r in range(rows):
                    if r != pivot_row and matrix[r][col] != 0:
                        matrix = add_scaled_row(matrix, pivot_row, r, -matrix[r][col])
                pivot_row += 1
        return matrix

    def swap_rows(matrix, r1, r2):
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        return matrix

    def scale_row(matrix, row, scalar):
        matrix[row] = [val * scalar for val in matrix[row]]
        return matrix

    def add_scaled_row(matrix, src_row, target_row, scalar):
        matrix[target_row] = [matrix[target_row][i] + scalar * matrix[src_row][i] for i in range(len(matrix[0]))]
        return matrix

    def extract_basis(matrix):
        basis = []
        for row in matrix:
            if any(value != 0 for value in row):
                basis.append(row)
        return basis

    matrix = [vector[:] for vector in S]
    reduced_matrix = row_echelon_form(matrix)
    basis = extract_basis(reduced_matrix)
    return len(basis), basis

S_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

dim, basis = dim_and_basis(S_example)
print("Dimension of the subspace:", dim)
print("Basis for the subspace:")
for vec in basis:
    print(vec)
