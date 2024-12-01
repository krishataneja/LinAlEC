class Matrix:
    def __init__(self, row_count, col_count, element_type="real"):
        
        if element_type not in ["real", "complex"]:
            raise ValueError("element must be real or complex")

        self.rows = row_count
        self.cols = col_count
        self.type = element_type
        self.matrix = [[0] * col_count for _ in range(row_count)]

    def set_entries(self, data):
       
        if len(data) != self.rows * self.cols:
            raise ValueError(f"Expected {self.rows * self.cols} values, but got {len(data)}.")

       
        idx = 0
        for r in range(self.rows):
            for c in range(self.cols):
                value = data[idx]
                if self.type == "real" and not isinstance(value, (int, float)):
                    raise TypeError("only real numbers")
                if self.type == "complex" and not isinstance(value, (int, float, complex)):
                    raise TypeError("only complex number")
                self.matrix[r][c] = value
                idx += 1

    def show_dimensions(self):
        
        return self.rows, self.cols

    def print_matrix(self):
       
        print("Matrix:")
        for row in self.matrix:
            row_str = " | ".join(str(x) for x in row)
            print(row_str)

    def __str__(self):
       
        return "\n".join(" | ".join(str(x) for x in row) for row in self.matrix)



if __name__ == "__main__":
    
    real_mat = Matrix(2, 3, element_type="real")
    real_mat.set_entries([1.2, -3.4, 5.6, 7.8, 9.0, -1.1])
    print("Real Matrix:")
    real_mat.print_matrix()

  
    complex_mat = Matrix(3, 2, element_type="complex")
    complex_mat.set_entries([2 + 3j, -4j, 1 + 5j, 0, -3.2, 4 + 6j])
    print("\nComplex Matrix:")
    print(complex_mat)
