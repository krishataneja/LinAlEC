class Matrix:
    def __init__(self, num_rows, num_cols, field_type="real"):
        """
        Initialize a matrix with the specified number of rows and columns.
        """
        if field_type not in ["real", "complex"]:
            raise ValueError("Field type must be 'real' or 'complex'.")

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.type = field_type
        self.elements = [[0] * num_cols for _ in range(num_rows)]

    def initialize_with_columns(self, column_vectors):
        """
        Initialize the matrix using column vectors.
        """
        if len(column_vectors) != self.num_cols:
            raise ValueError(f"Expected {self.num_cols} columns, got {len(column_vectors)}.")

        # Check that each column is of correct length
        for idx, column in enumerate(column_vectors):
            if len(column) != self.num_rows:
                raise ValueError(f"Column {idx + 1} does not have {self.num_rows} rows.")
            if self.type == "real" and any(not isinstance(value, (int, float)) for value in column):
                raise TypeError("All elements in real field columns must be numbers.")
            if self.type == "complex" and any(not isinstance(value, (int, float, complex)) for value in column):
                raise TypeError("All elements in complex field columns must be numbers or complex.")

        # Populate the matrix column by column
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
        """
        Return string representation of the matrix.
        """
        return "\n".join(" | ".join(map(str, row)) for row in self.elements)

    def __add__(self, other):
        """
        Handle matrix addition using the '+' operator.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions to add them.")

        result_matrix = Matrix(self.num_rows, self.num_cols, self.type)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result_matrix.elements[i][j] = self.elements[i][j] + other.elements[i][j]
        return result_matrix

    def __mul__(self, other):
        """
        Handle matrix multiplication using the '*' operator.
        """
        if self.num_cols != other.num_rows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")

        product_matrix = Matrix(self.num_rows, other.num_cols, self.type)
        for i in range(self.num_rows):
            for j in range(other.num_cols):
                product_matrix.elements[i][j] = sum(self.elements[i][k] * other.elements[k][j] for k in range(self.num_cols))
        return product_matrix


# Example Usage
if __name__ == "__main__":
    # 1. Real Matrix Addition
    print("Initializing two 2x2 Real Matrices for Addition:")
    mat_1 = Matrix(2, 2, "real")
    mat_1.initialize_with_columns([[1, 3], [2, 4]])
    
    mat_2 = Matrix(2, 2, "real")
    mat_2.initialize_with_columns([[5, 7], [6, 8]])

    try:
        sum_matrix = mat_1 + mat_2
        print("Result of Real Matrix Addition:")
        sum_matrix.display()
    except ValueError as error:
        print(f"Error: {error}")

    # 2. Real Matrix Multiplication
    print("\nInitializing two 2x2 Real Matrices for Multiplication:")
    mat_3 = Matrix(2, 2, "real")
    mat_3.initialize_with_columns([[1, 2], [3, 4]])

    mat_4 = Matrix(2, 2, "real")
    mat_4.initialize_with_columns([[5, 6], [7, 8]])

    try:
        product_matrix = mat_3 * mat_4
        print("Result of Real Matrix Multiplication:")
        product_matrix.display()
    except ValueError as error:
        print(f"Error: {error}")

    # 3. Complex Matrix Multiplication
    print("\nInitializing two 2x2 Complex Matrices for Multiplication:")
    mat_5 = Matrix(2, 2, "complex")
    mat_5.initialize_with_columns([[1 + 2j, 2 + 3j], [3 + 4j, 4 + 5j]])

    mat_6 = Matrix(2, 2, "complex")
    mat_6.initialize_with_columns([[5 + 6j, 6 - 7j], [7 + 8j, 9 + 10j]])

    try:
        complex_product = mat_5 * mat_6
        print("Result of Complex Matrix Multiplication:")
        complex_product.display()
    except ValueError as error:
        print(f"Error: {error}")
