class Matrix:
    def __init__(self, num_rows, num_cols, field_type="real"):
     
        if field_type not in ["real", "complex"]:
            raise ValueError("field must be complex or reak”)

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.type = field_type
        self.elements = [[0] * num_cols for _ in range(num_rows)]

    def initialize_with_columns(self, column_vectors):
       
        if len(column_vectors) != self.num_cols:
            raise ValueError(f"xrpected {self.num_cols} columns, got {len(column_vectors)}.")

        # Check that each column is of correct length
        for idx, column in enumerate(column_vectors):
            if len(column) != self.num_rows:
                raise ValueError(f"Column {idx + 1} does not have {self.num_rows} rows.")
            if self.type == "real" and any(not isinstance(value, (int, float)) for value in column):
                raise TypeError("must be real.")
            if self.type == "complex" and any(not isinstance(value, (int, float, complex)) for value in column):
                raise TypeError("must be complex”)
      
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                self.elements[r][c] = column_vectors[c][r]

    def display(self):
        """
        Print the matrix in a structured format.
        """
        for row in self.elements:
            print(" | ".join(map(str, row)))

    def __str__(self):
      
        return "\n".join(" | ".join(map(str, row)) for row in self.elements)

    def __add__(self, other):
        
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions to add them.")

        result_matrix = Matrix(self.num_rows, self.num_cols, self.type)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result_matrix.elements[i][j] = self.elements[i][j] + other.elements[i][j]
        return result_matrix

    def __mul__(self, other):
      
        if self.num_cols != other.num_rows:
            raise ValueError("no of columns must be = to rows")

        product_matrix = Matrix(self.num_rows, other.num_cols, self.type)
        for i in range(self.num_rows):
            for j in range(other.num_cols):
                product_matrix.elements[i][j] = sum(self.elements[i][k] * other.elements[k][j] for k in range(self.num_cols))
        return product_matrix

    def get_row(self, row_index):        if row_index < 0 or row_index >= self.num_rows:
            raise IndexError("Row index is out of bounds.")
        return self.elements[row_index]

    def get_column(self, col_index):
      
        if col_index < 0 or col_index >= self.num_cols:
            raise IndexError("Column index is out of bounds.")
        return [self.elements[row][col_index] for row in range(self.num_rows)]

    def multiply_row_and_column(self, row_index, col_index):
        
        if row_index < 0 or row_index >= self.num_rows or col_index < 0 or col_index >= self.num_cols:
            raise IndexError("Row or column index is out of bounds.")
        
        row = self.get_row(row_index)
        col = self.get_column(col_index)

        # Dot product of the row and column
        result = sum(row[i] * col[i] for i in range(len(row)))
        return result



if __name__ == "__main__":
  
    print("Initializing a 3x3 Matrix with Real Numbers:")
    matrix_data = Matrix(3, 3, "real")
    matrix_data.initialize_with_columns([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


    matrix_data.display()


    print("\nRow 1 of the matrix:", matrix_data.get_row(0))
    print("column 2 of the matrix:", matrix_data.get_column(1))


    row_index = 0
    col_index = 1
    scalar_result = matrix_data.multiply_row_and_column(row_index, col_index)
    print(f"\nDot product of Row {row_index + 1} and Column {col_index + 1}: {scalar_result}")
