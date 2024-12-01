class Matrix:
    def __init__(self, row_count, column_count, field="real"):
      
        if field not in ["real", "complex"]:
            raise ValueError("must be real or xomplex")

        self.rows = row_count
        self.columns = column_count
        self.field_type = field
        self.matrix_data = [[0] * column_count for _ in range(row_count)]

    def populate_from_columns(self, column_vectors):
        
        if len(column_vectors) != self.columns:
            raise ValueError(f"Expected {self.columns} columns, got {len(column_vectors)}.")
        
        for i, vector in enumerate(column_vectors):
            if len(vector) != self.rows:
                raise ValueError(f"Column {i + 1} does not have {self.rows} rows.")
            if self.field_type == "real" and any(not isinstance(val, (int, float)) for val in vector):
                raise TypeError("must be numeric.")
            if self.field_type == "complex" and any(not isinstance(val, (int, float, complex)) for val in vector):
                raise TypeError(“error: must be numeric or complex.")


        for j in range(self.columns):
            for i in range(self.rows):
                self.matrix_data[i][j] = column_vectors[j][i]

    def show(self):
       
        for row in self.matrix_data:
            print(" | ".join(map(str, row)))

    def __str__(self):
       
        return "\n".join(" | ".join(map(str, row)) for row in self.matrix_data)

    def __add__(self, other):
       
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Both matrices must have the same dimensions to add them.")

        result_matrix = Matrix(self.rows, self.columns, self.field_type)
        for i in range(self.rows):
            for j in range(self.columns):
                result_matrix.matrix_data[i][j] = self.matrix_data[i][j] + other.matrix_data[i][j]
        return result_matrix

    def __mul__(self, other):
       
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")

        product_matrix = Matrix(self.rows, other.columns, self.field_type)
        for i in range(self.rows):
            for j in range(other.columns):
                product_matrix.matrix_data[i][j] = sum(self.matrix_data[i][k] * other.matrix_data[k][j] for k in range(self.columns))
        return product_matrix

    def transpose(self):
        
        transposed_matrix = Matrix(self.columns, self.rows, self.field_type)
        for i in range(self.rows):
            for j in range(self.columns):
                transposed_matrix.matrix_data[j][i] = self.matrix_data[i][j]
        return transposed_matrix

    def conjugate(self):
       
        conjugated_matrix = Matrix(self.rows, self.columns, self.field_type)
        for i in range(self.rows):
            for j in range(self.columns):
                if isinstance(self.matrix_data[i][j], complex):
                    conjugated_matrix.matrix_data[i][j] = self.matrix_data[i][j].conjugate()
                else:
                    conjugated_matrix.matrix_data[i][j] = self.matrix_data[i][j]
        return conjugated_matrix

    def transpose_conjugate(self):
        
        return self.transpose().conjugate()



if __name__ == "__main__":
    
    print("initializing a 2x2 Complex Matrix:")
    complex_matrix = Matrix(2, 2, "complex")
    complex_matrix.populate_from_columns([[1 + 2j, 3 + 4j], [5 + 6j, 7 + 8j]])


    print("og matrix:")
    complex_matrix.show()


    transposed = complex_matrix.transpose()
    print("\ntransposed Matrix:")
    transposed.show()


    conjugated = complex_matrix.conjugate()
    print("\nconjugated Matrix:")
    conjugated.show()


    trans_conj = complex_matrix.transpose_conjugate()
    print("\nT-CMatrix:")
    trans_conj.show()
