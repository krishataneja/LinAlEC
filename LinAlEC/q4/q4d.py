def is_subsp(S1, S2):
    def row_reduce(matrix):
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
                factor = 1 / matrix[pivot_row][col]
                matrix = scale_row(matrix, pivot_row, factor)
                for r in range(rows):
                    if r != pivot_row and matrix[r][col] != 0:
                        matrix = eliminate_row(matrix, pivot_row, r, -matrix[r][col])
                pivot_row += 1
        return matrix

    def swap_rows(matrix, r1, r2):
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        return matrix

    def scale_row(matrix, row, scalar):
        matrix[row] = [val * scalar for val in matrix[row]]
        return matrix

    def eliminate_row(matrix, src_row, target_row, scalar):
        matrix[target_row] = [matrix[target_row][i] + scalar * matrix[src_row][i] for i in range(len(matrix[0]))]
        return matrix

    def is_vector_in_span(vec, span):
        extended_matrix = [row[:] for row in span] + [vec]
        reduced_matrix = row_reduce(extended_matrix)
        last_row = reduced_matrix[-1]
        return all(value == 0 for value in last_row)

    for vec in S1:
        if not is_vector_in_span(vec, S2):
            return False
    return True

ex1= [
    [1, 2, 3],
    [4, 5, 6]
]

ex2 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

result = is_subsp(ex1, ex2)
print("Is S1 a subspace of S2?", result)
