def det_PLU(A):
    try:
        n = len(A)
        if n != len(A[0]):
            return "must be a square matrix"

        def swap(A, row1, row2):
            A[row1], A[row2] = A[row2], A[row1]

        def scale(A, row, factor):
            A[row] = [x * factor for x in A[row]]

        def rref(A):
            row_operations = 0
            scaling_factor = 1
            for i in range(n):
                if A[i][i] == 0:
                    for j in range(i + 1, n):
                        if A[j][i] != 0:
                            swap(A, i, j)
                            scaling_factor *= -1
                            row_operations += 1
                            break
                pivot = A[i][i]
                if pivot != 0:
                    scale(A, i, 1 / pivot)
                    scaling_factor *= pivot
                for j in range(i + 1, n):
                    if A[j][i] != 0:
                        factor = A[j][i]
                        A[j] = [A[j][k] - factor * A[i][k] for k in range(n)]
            for i in range(n - 1, -1, -1):
                for j in range(i - 1, -1, -1):
                    if A[j][i] != 0:
                        factor = A[j][i]
                        A[j] = [A[j][k] - factor * A[i][k] for k in range(n)]
            return A, scaling_factor

        rref_matrix, scaling_factor = rref(A)
        det = scaling_factor
        for i in range(n):
            det *= rref_matrix[i][i]
        return det

    except Exception as e:
        return f"errror: {e}"

m1 = [[4, 7], [2, 6]]
m2 = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]

print(det_PLU(m1))
print(det_PLU(m2))

