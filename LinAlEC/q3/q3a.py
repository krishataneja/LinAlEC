
def vector_length(v):
    total = 0
    for element in v:
        total += element**2
    return total**0.5


def matrix_size(A):
    num_rows = len(A)
    num_columns = len(A[0]) if num_rows > 0 else 0
    return (num_rows, num_columns)


def matrix_rank(A):
    
    def row_echelon_form(matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        row = 0
        
        for col in range(columns):
            if row >= rows:
                break
            if matrix[row][col] == 0:
                for i in range(row + 1, rows):
                    if matrix[i][col] != 0:
                        matrix[row], matrix[i] = matrix[i], matrix[row]
                        break
            if matrix[row][col] != 0:
            
                pivot = matrix[row][col]
                for j in range(col, columns):
                    matrix[row][j] /= pivot
                
                for i in range(row + 1, rows):
                    factor = matrix[i][col]
                    for j in range(col, columns):
                        matrix[i][j] -= factor * matrix[row][j]
                row += 1
        return matrix
    
    echelon_matrix = [row[:] for row in A]
    row_echelon_form(echelon_matrix)
    

    rank = 0
    for row in echelon_matrix:
        if any(cell != 0 for cell in row):
            rank += 1
    return rank

def matrix_nullity(A):
    rows, columns = matrix_size(A)
    rank = matrix_rank(A)
    return columns - rank


v_example = [3, 4, 12]  
A_example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print("Length of the vector v:", vector_length(v_example))
print("Size of the matrix A:", matrix_size(A_example))
print("Rank of the matrix A:", matrix_rank(A_example))
print("Nullity of the matrix A:", matrix_nullity(A_example))
