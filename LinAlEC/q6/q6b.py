def express_in_span(S, v):
    def subtract_vectors(A, B):
        return [a - b for a, b in zip(A, B)]

    def dot_product(X, Y):
        return sum(x * y for x, y in zip(X, Y))

    def row_echelon_form(A):
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

    def back_substitution(A, b):
        n = len(b)
        x = [0] * n
        for i in range(n - 1, -1, -1):
            sum_terms = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum_terms) / A[i][i]
        return x

    def augmented_matrix(S, v):
        return [row + [b] for row, b in zip(S, v)]

    size = len(S)
    augmented = augmented_matrix(S, v)
    row_echelon_matrix = row_echelon_form([row[:] for row in augmented])
    coeffs = back_substitution(row_echelon_matrix, [row[-1] for row in row_echelon_matrix])
    return coeffs

S = [[2, 1], [1, 2]]
v = [3, 5]
print("v in terms of S:", express_in_span(S, v))
