def rank_factorization(A):
    def row_reduce(matrix):
        rows, cols = len(matrix), len(matrix[0])
        pivot_row = 0
        for col in range(cols):
            if pivot_row >= rows:
                break
            if matrix[pivot_row][col] == 0:
                for r in range(pivot_row + 1, rows):
                    if matrix[r][col] != 0:
                        matrix = swap(matrix, pivot_row, r)
                        break
            if matrix[pivot_row][col] != 0:
                factor = 1 / matrix[pivot_row][col]
                matrix = scale(matrix, pivot_row, factor)
                for r in range(rows):
                    if r != pivot_row and matrix[r][col] != 0:
                        matrix = eliminate(matrix, pivot_row, r, -matrix[r][col])
                pivot_row += 1
        return matrix

    def swap(matrix, r1, r2):
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        return matrix

    def scale(matrix, row, scalar):
        matrix[row] = [val * scalar for val in matrix[row]]
        return matrix

    def eliminate(matrix, src_row, target_row, scalar):
        matrix[target_row] = [matrix[target_row][i] + scalar * matrix[src_row][i] for i in range(len(matrix[0]))]
        return matrix

    def extract_columns(matrix, col_indices):
        cols = [[matrix[r][c] for r in range(len(matrix))] for c in col_indices]
        return [[cols[c][r] for c in range(len(cols))] for r in range(len(cols[0]))]

    def find_pivot_columns(matrix):
        rows, cols = len(matrix), len(matrix[0])
        pivot_columns = []
        pivot_row = 0
        for col in range(cols):
            if pivot_row >= rows:
                break
            if matrix[pivot_row][col] != 0:
                pivot_columns.append(col)
                pivot_row += 1
        return pivot_columns

    row_reduced = row_reduce([row[:] for row in A])
    pivot_cols = find_pivot_columns(row_reduced)
    U = extract_columns(A, pivot_cols)
    R = [[row[col] for col in pivot_cols] for row in row_reduced if any(value != 0 for value in row)]
    return U, R

A_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

U, R = rank_factorization(A_example)
print("U (Independent Columns):")
for row in U:
    print(row)
print("R (Row Reduced Form):")
for row in R:
    print(row)
