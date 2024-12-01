def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for i in range(size):
        sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        det += ((-1) ** i) * matrix[0][i] * determinant(sub_matrix)
    return det

def row_echelon(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        if matrix[i][i] == 0:
            for j in range(i + 1, rows):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
        if matrix[i][i] != 0:
            for j in range(i + 1, rows):
                factor = matrix[j][i] / matrix[i][i]
                matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(cols)]
    return matrix

def algebraic_multiplicity(matrix, eigenvalue):
    size = len(matrix)
    identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    modified_matrix = [[matrix[i][j] - (eigenvalue if i == j else 0) for j in range(size)] for i in range(size)]
    
 
    return determinant(modified_matrix)

def geometric_multiplicity(matrix, eigenvalue):
    size = len(matrix)
    identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    reduced_matrix = [[matrix[i][j] - (eigenvalue if i == j else 0) for j in range(size)] for i in range(size)]
    
   
    row_echelon_matrix = row_echelon([row[:] for row in reduced_matrix])
    rank = sum(1 for row in row_echelon_matrix if any(abs(x) > 1e-9 for x in row))
    
    return size - rank  

def eigen_basis(matrix, eigenvalue):
    size = len(matrix)
    identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    reduced_matrix = [[matrix[i][j] - (eigenvalue if i == j else 0) for j in range(size)] for i in range(size)]
    
    
    row_echelon_matrix = row_echelon([row[:] for row in reduced_matrix])
    
   
    eigenvectors = []
    for i in range(size):
        if all(abs(x) < 1e-9 for x in row_echelon_matrix[i]):
            eigenvectors.append([1 if j == i else 0 for j in range(size)])
    
    return eigenvectors

matrix = [[2, 1], [1, 2]]
eigenvalue = 3

print("Algebraic Multiplicity:", algebraic_multiplicity(matrix, eigenvalue))
print("Geometric Multiplicity:", geometric_multiplicity(matrix, eigenvalue))
print("Eigenbasis:", eigen_basis(matrix, eigenvalue))
