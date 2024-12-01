def coord(B, v):
    def row_reduce(A):
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
        result = [0] * n
        for i in range(n - 1, -1, -1):
            subtotal = sum(A[i][j] * result[j] for j in range(i + 1, n))
            result[i] = (b[i] - subtotal) / A[i][i]
        return result

    def create_augmented_matrix(B, v):
        return [row + [b] for row, b in zip(B, v)]

    augmented = create_augmented_matrix(B, v)
    row_reduced = row_reduce([row[:] for row in augmented])
    coords = back_substitution(row_reduced, [row[-1] for row in row_reduced])
    return coords

def vector_from_coords(B, coords):
    return [sum(B[i][j] * coords[j] for j in range(len(coords))) for i in range(len(B))]

B = [[2, 1], [1, 2]]
v = [3, 5]
coordinates = coord(B, v)
print("v wrt B", coordinates)

reconstructed_vector = vector_from_coords(B, coordinates)
print("reconstructed vectors", reconstructed_vector)
