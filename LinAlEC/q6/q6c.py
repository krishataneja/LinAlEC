def span_equal(S1, S2):
    def augment_matrices(A, B):
        return [row + [b] for row, b in zip(A, B)]

    def subtract_rows(A, B):
        return [a - b for a, b in zip(A, B)]

    def echelon_process(A):
        rows = len(A)
        cols = len(A[0])
        for i in range(rows):
            if A[i][i] == 0:
                for j in range(i + 1, rows):
                    if A[j][i] != 0:
                        A[i], A[j] = A[j], A[i]
                        break
            if A[i][i] != 0:
                for j in range(i + 1, rows):
                    factor = A[j][i] / A[i][i]
                    A[j] = [A[j][k] - factor * A[i][k] for k in range(cols)]
        return A

    def back_solve(A, b):
        n = len(b)
        result = [0] * n
        for i in range(n - 1, -1, -1):
            subtotal = sum(A[i][j] * result[j] for j in range(i + 1, n))
            result[i] = (b[i] - subtotal) / A[i][i]
        return result

    def find_null_space(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if not any(matrix[i]):
                yield [1 if j == i else 0 for j in range(cols)]

    def compare_sets(S1, S2):
        augmented1 = augment_matrices(S1, [0] * len(S1))
        augmented2 = augment_matrices(S2, [0] * len(S2))
        rref1 = echelon_process([row[:] for row in augmented1])
        rref2 = echelon_process([row[:] for row in augmented2])
        
        null_space1 = set(map(tuple, find_null_space(rref1)))
        null_space2 = set(map(tuple, find_null_space(rref2)))

        return null_space1 == null_space2

    return compare_sets(S1, S2)

S1 = [[2, 1], [1, 2]]
S2 = [[1, 3], [2, 1]]
print("same subspace:", span_equal(S1, S2))
