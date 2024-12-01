class LinearSystem:
    def __init__(self, A, b):
        self.A = A
        self.b = b
        if len(A) != len(b):
            raise ValueError("Error: Number of rows in A must match the size of b.")
        for row in A:
            if len(row) != len(A[0]):
                raise ValueError("Error: All rows in A must have the same number of columns.")

    def is_consistent(self):
        augmented_matrix = [row + [self.b[i]] for i, row in enumerate(self.A)]
        reduced_matrix = self.row_reduce(augmented_matrix)
        for row in reduced_matrix:
            if all(value == 0 for value in row[:-1]) and row[-1] != 0:
                return False
        return True

    def find_solution(self):
        if not self.is_consistent():
            return "Error: System is inconsistent, no solution exists."
        augmented_matrix = [row + [self.b[i]] for i, row in enumerate(self.A)]
        reduced_matrix = self.row_reduce(augmented_matrix)
        solution = [0] * len(self.A[0])
        for i in range(len(solution) - 1, -1, -1):
            solution[i] = reduced_matrix[i][-1]
            for j in range(i + 1, len(solution)):
                solution[i] -= reduced_matrix[i][j] * solution[j]
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
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
b_example = [8, -11, -3]

try:
    system = LinearSystem(A_example, b_example)
    if system.is_consistent():
        solution = system.find_solution()
        print("Solution to the system:", solution)
    else:
        print("The system is inconsistent.")
except ValueError as e:
    print(e)
