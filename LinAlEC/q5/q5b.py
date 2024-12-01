def det_rref(matrix_XY):
    
    if len(matrix_XY) != len(matrix_XY[0]):
        return "matrix must be sqaure"
    
    try:
       
        scaling_factor = 1
        row_swaps_count = 0
        working_matrix = [row[:] for row in matrix_XY]  

  
        for current_row in range(len(working_matrix)):
            if working_matrix[current_row][current_row] == 0:
                for next_row in range(current_row + 1, len(working_matrix)):
                    if working_matrix[next_row][current_row] != 0:
                      
                        working_matrix[current_row], working_matrix[next_row] = (
                            working_matrix[next_row],
                            working_matrix[current_row],
                        )
                        row_swaps_count += 1
                        break
            
    
            pivot_element = working_matrix[current_row][current_row]
            if pivot_element != 0:
                scaling_factor *= pivot_element
                working_matrix[current_row] = [
                    element / pivot_element for element in working_matrix[current_row]
                ]
            

            for below_row in range(current_row + 1, len(working_matrix)):
                factor_to_reduce = working_matrix[below_row][current_row]
                working_matrix[below_row] = [
                    below - factor_to_reduce * above
                    for below, above in zip(
                        working_matrix[below_row], working_matrix[current_row]
                    )
                ]
        
        
        determinant_value = scaling_factor * (-1) ** row_swaps_count
        return determinant_value

    except Exception as e:
        return f"Error in determinant computation: {e}"


matrix_3 = [[2, 1, 3], [1, 1, 1], [3, 2, 4]]
print(det_rref(matrix_3))
