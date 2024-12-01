class Matrix:
    def __init__(self, row_count, col_count, element_type="real"):
        """
        Initialize a matrix with specified dimensions and element type.
        """
        if element_type not in ["real", "complex"]:
            raise ValueError("Element type must be 'real' or 'complex'.")

        self.row_total = row_count
        self.col_total = col_count
        self.field = element_type
        self.data = [[0] * col_count for _ in range(row_count)]

    def set_columns(self, column_vectors):
        """
        Initialize the matrix using column vectors.
        """
        if len(column_vectors) != self.col_total:
            raise ValueError(f"Expected {self.col_total} column vectors, but received {len(column_vectors)}.")

        # Validate that all vectors have the correct length
        for idx, column in enumerate(column_vectors):
            if len(column) != self.row_total:
                raise ValueError(f"Column {idx + 1} does not have {self.row_total} elements.")
            if self.field == "real" and any(not isinstance(item, (int, float)) for item in column):
                raise TypeError("All values in real field columns must be real numbers.")
            if self.field == "complex" and any(not isinstance(item, (int, float, complex)) for item in column):
                raise TypeError("All values in complex field columns must be complex numbers.")

        # Populate the matrix column by column
        for col_idx, col_data in enumerate(column_vectors):
            for row_idx, value in enumerate(col_data):
                self.data[row_idx][col_idx] = value

    def print_matrix(self):
        """
        Print the matrix in a structured format.
        """
        print("Matrix:")
        for row in self.data:
            print(" | ".join(map(str, row)))

    def __str__(self):
        """
        String representation of the matrix.
        """
        return "\n".join(" | ".join(map(str, row)) for row in self.data)


# Example Usage
if __name__ == "__main__":
    # Example 1: Real Matrix Initialization with Columns
    print("Initializing a 3x2 Real Matrix using columns:")
    real_columns = [
        [1.0, 2.0, 3.0],  # First column
        [-4.0, 5.0, 6.0]  # Second column
    ]
    real_matrix = Matrix(3, 2, element_type="real")
    real_matrix.set_columns(real_columns)
    real_matrix.print_matrix()

    # Example 2: Complex Matrix Initialization with Columns
    print("\nInitializing a 2x3 Complex Matrix using columns:")
    complex_columns = [
        [1 + 1j, 2 + 2j],  # First column
        [-3j, 4],          # Second column
        [5 - 1j, 6 + 0j]   # Third column
    ]
    complex_matrix = Matrix(2, 3, element_type="complex")
    complex_matrix.set_columns(complex_columns)
    complex_matrix.print_matrix()
