
def rref(A, show_operations=False):
   
    def swap_rows(matrix, r1, r2):
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        return matrix
    
    
    def scale_row(matrix, row, scalar):
        matrix[row] = [elem * scalar for elem in matrix[row]]
        return matrix
    
    
    def add_scaled_row(matrix, row_to_add, row_to_which, scalar):
        matrix[row_to_which] = [matrix[row_to_which][i] + scalar * matrix[row_to_add][i] for i in range(len(matrix[0]))]
        return matrix
    
    rows = len(A)
    cols = len(A[0])
    matrix = [row[:] for row in A]  
    operations = [] 
    elementary_matrices = []  
    
    pivot_row = 0  
    
    for col in range(cols):
        if pivot_row >= rows:
            break
      
        if matrix[pivot_row][col] == 0:
            for r in range(pivot_row + 1, rows):
                if matrix[r][col] != 0:
                    matrix = swap_rows(matrix, pivot_row, r)
                    if show_operations:
                        operations.append(f"Swap row {pivot_row + 1} with row {r + 1}")
                        elementary_matrices.append(create_elementary_matrix_swap(rows, col, pivot_row, r))
                    break
        if matrix[pivot_row][col] != 0:
            pivot = matrix[pivot_row][col]
            matrix = scale_row(matrix, pivot_row, 1 / pivot)
            if show_operations:
                operations.append(f"Scale row {pivot_row + 1} by {1 / pivot}")
                elementary_matrices.append(create_elementary_matrix_scale(rows, col, pivot_row, 1 / pivot))
            
           
            for r in range(rows):
                if r != pivot_row and matrix[r][col] != 0:
                    scalar = -matrix[r][col]
                    matrix = add_scaled_row(matrix, pivot_row, r, scalar)
                    if show_operations:
                        operations.append(f"Add {scalar} * row {pivot_row + 1} to row {r + 1}")
                        elementary_matrices.append(create_elementary_matrix_add(rows, col, pivot_row, r, scalar))
            pivot_row += 1
    
    if show_operations:
        print("Row Operations:")
        for op in operations:
            print(op)
    
    if show_operations:
        print("\nElementary Matrices:")
        for mat in elementary_matrices:
            print(mat)
    
    return matrix

def create_elementary_matrix_swap(rows, col, r1, r2):
    E = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
    E[r1][r1], E[r1][r2] = E[r2][r2], E[r1][r1]
    E[r2][r1], E[r2][r2] = E[r1][r2], E[r2][r1]
    return E


def create_elementary_matrix_scale(rows, col, row, scalar):
    E = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
    E[row][row] = scalar
    return E


def create_elementary_matrix_add(rows, col, row_to_add, row_to_which, scalar):
    E = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
    E[row_to_which][col] = scalar
    return E


matrix_example = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]


rref_matrix = rref(matrix_example)
print("RREF:")
for row in rref_matrix:
    print(row)
    
rref_matrix_with_operations = rref(matrix_example, show_operations=True)
print("\nRREF with row operations and elementary matrices:")
for row in rref_matrix_with_operations:
    print(row)
