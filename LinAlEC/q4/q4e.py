class LinearSystem:
    def __init__(self, A, b):
        self.A = A
        self.b = b
        if len(A) != len(b):
            raise ValueError("Error: Number of rows in A must match the size of b.")
        for row in A:
            if len(row) != len(A[0]):
                raise ValueError("Error: All rows in A must have the same number of columns.")

    def solution_set(self):
        augmented_matrix = [row + [self.b[i]] for i, row in enumerate(self.A)]
        rref_matrix = self.row_reduce(augmented_matrix)
        num_rows, num_cols = len(rref_matrix), len(rref_matrix[0]) - 1
        pivot_cols = []
        free_vars = []

        for i in range(num_rows):
            for j in range(num_cols):
                if rref_matrix[i][j] != 0:
                    pivot_cols.append(j)
                    break

        free_vars = [col for col in range(num_cols) if col not in pivot_cols]

        solution = [None] * num_cols
        for i in range(num_cols):
            if i in free_vars:
                solution[i] = f"Free variable x{i}"
            else:
                sol = rref_matrix[pivot_cols.index(i)][-1]
                for j in free_vars:
                    sol -= rref_matrix[pivot_cols.index(i)][j] * 0  # Free variables should contribute 0 to this equation
                solution[i] = sol

        return solution

    def row_reduce(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        pivot_row = 0
        for col in range(cols - 1):
            if pivot_row >= rows:
                break
            if matrix[pivot_row][col] == 0:
                for r in range(pivot_row + 1, rows):
                    if matrix[r][col] != 0:
                        matrix = self.swap_rows(matrix, pivot_row, r)
                        break
            if matrix[pivot_row][col] != 0:
                factor = 1 / matrix[pivot_row][col]
                matrix = self.scale_row(matrix, pivot_row, factor)
                for r in range(rows):
                    if r != pivot_row and matrix[r][col] != 0:
                        matrix = self.eliminate_row(matrix, pivot_row, r, -matrix[r][col])
                pivot_row += 1
        return matrix

    def swap_rows(self, matrix, r1, r2):
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        return matrix

    def scale_row(self, matrix, row, factor):
        matrix[row] = [val * factor for val in matrix[row]]
        return matrix

    def eliminate_row(self, matrix, src_row, target_row, factor):
        matrix[target_row] = [matrix[target_row][i] + factor * matrix[src_row][i] for i in range(len(matrix[0]))]
        return matrix

# Example usage
A_example = [
    [1, 1, 0],
    [0, 1, 1]
]
b_example = [5, 7]

try:
    system = LinearSystem(A_example, b_example)
    solution = system.solution_set()
    print("Solution set:")
    for sol in solution:
        print(sol)
except ValueError as e:
    print(e)
