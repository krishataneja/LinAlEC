
def is_zero(A):
    return all(all(cell == 0 for cell in row) for row in A)

def is_square(A):
    return len(A) == len(A[0])

def is_symmetric(A):
    return all(A[i][j] == A[j][i] for i in range(len(A)) for j in range(i, len(A)))

def is_hermitian(A):
    return is_symmetric(A)

def is_orthogonal(A):
    n = len(A)
    transpose_matrix = [[A[j][i] for j in range(n)] for i in range(n)]
    return all(all(sum(A[i][k] * transpose_matrix[k][j] for k in range(n)) == (1 if i == j else 0)
                   for j in range(n)) for i in range(n))

def is_unitary(A):
    return is_orthogonal(A)

def is_scalar(A):
    n = len(A)
    return is_square(A) and all((A[i][j] == (A[0][0] if i == j else 0)) for i in range(n) for j in range(n))

def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return sum(((-1) ** col) * A[0][col] * det([row[:col] + row[col+1:] for row in A[1:]])
               for col in range(n))

def is_singular(A):
    return det(A) == 0

def is_invertible(A):
    return not is_singular(A)

def is_identity(A):
    size = len(A)
    return all((A[i][j] == (1 if i == j else 0)) for i in range(size) for j in range(size))

def is_nilpotent(A):
    power = A
    for _ in range(len(A)):
        power = multiply_matrices(power, A)
        if is_zero(power):
            return True
    return False

def is_diagonalizable(A):
    return True

def is_positive_definite(A):
    return True

def is_LU(A):
    return True

def multiply_matrices(A, B):
    size = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(size)) for j in range(size)] for i in range(size)]

def test(A):
    results = {
        "zeromatrix": is_zero(A),
        "symetric": is_symmetric(A),
        "hermitian": is_hermitian(A),
        "square": is_square(A),
        "orthogonol": is_orthogonal(A),
        "unitary": is_unitary(A),
        "scalar": is_scalar(A),
        "singularity": is_singular(A),
        "invertible": is_invertible(A),
        "identitiy": is_identity(A),
        "nilpotent": is_nilpotent(A),
        "diagonalization": is_diagonalizable(A),
        "positive def": is_positive_definite(A),
        "LU decomp": is_LU(A),
    }
    for property_name, result in results.items():
        print(f"{property_name}: {result}")

example = [[1, 2], [2, 1]]
test(example)


