
def is_li(S):
  
    def row_echelon(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        pivot_row = 0  
        
        for col in range(cols):
            if pivot_row >= rows:
                break
           
            if matrix[pivot_row][col] == 0:
                for r in range(pivot_row + 1, rows):
                    if matrix[r][col] != 0:
                        matrix = swap_rows(matrix, pivot_row, r)
                        break
            if matrix[pivot_row][col] != 0:
                pivot = matrix[pivot_row][col]
                matrix = scale_row(matrix, pivot_row, 1 / pivot)
                
                
                for r in range(rows):
                    if r != pivot_row and matrix[r][col] != 0:
                        scalar = -matrix[r][col]
                        matrix = add_scaled_row(matrix, pivot_row, r, scalar)
                pivot_row += 1
        
        return matrix


    def swap_rows(matrix, r1, r2):
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        return matrix
  
    def scale_row(matrix, row, scalar):
        matrix[row] = [elem * scalar for elem in matrix[row]]
        return matrix
    

    def add_scaled_row(matrix, row_to_add, row_to_which, scalar):
        matrix[row_to_which] = [matrix[row_to_which][i] + scalar * matrix[row_to_add][i] for i in range(len(matrix[0]))]
        return matrix


    matrix = [vector[:] for vector in S]  
    rows = len(matrix)
    cols = len(matrix[0])

    
    reduced_matrix = row_echelon(matrix)


    non_zero_rows = sum(1 for row in reduced_matrix if any(value != 0 for value in row))
    
    
    if non_zero_rows < len(S):
        return "Linearly Dependent"
    else:
        return "Linearly Independent"


S_example = [
    [1, 2, 3],  
    [4, 5, 6], 
    [7, 8, 9]   
]


result = is_li(S_example)
print(result)  
