def matrix_minor(matrix, row, col):
    return [r[:col] + r[col + 1:] for r in (matrix[:row] + matrix[row + 1:])]

def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for col in range(size):
        det += ((-1) ** col) * matrix[0][col] * determinant(matrix_minor(matrix, 0, col))
    return det

def characteristic_polynomial(matrix):
    n = len(matrix)
    coeffs = []
    for lam in range(n + 1):
        shifted_matrix = [[matrix[i][j] if i != j else matrix[i][j] - lam for j in range(n)] for i in range(n)]
        coeffs.append(determinant(shifted_matrix))
    return coeffs

def eigenvalues(matrix):
    def poly_eval(coeffs, x):
        return sum(coeffs[i] * (x ** i) for i in range(len(coeffs)))

    def derivative_eval(coeffs, x):
        return sum(i * coeffs[i] * (x ** (i - 1)) for i in range(1, len(coeffs)))

    coeffs = characteristic_polynomial(matrix)
    roots = []
    tolerance = 1e-6
    max_iterations = 100

    initial_guesses = [i + 1 for i in range(len(matrix))]

    for guess in initial_guesses:
        for _ in range(max_iterations):
            f_val = poly_eval(coeffs, guess)
            f_prime = derivative_eval(coeffs, guess)
            if abs(f_prime) < 1e-12:
                break
            correction = f_val / f_prime
            guess -= correction
            if abs(correction) < tolerance:
                break
        roots.append(round(guess, 6))
    return sorted(list(set(roots)))

m = [
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
]

eigen_vals = eigenvalues(m)
print("Eigenvalues:", eigen_vals)


